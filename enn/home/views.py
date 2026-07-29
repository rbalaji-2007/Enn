from django.shortcuts import render, redirect, get_object_or_404
# pyrefly: ignore [missing-import]
from .models import Transaction, UserSettings
import datetime
import json

def home(request):
    user_settings = UserSettings.get_settings()
    
    if request.method == "POST":
        amt = request.POST.get("amount")
        descrip = request.POST.get("descrip", "").strip()
        cat = request.POST.get("category", "miscellaneous")
        date_val = request.POST.get("date")
        
        # Check if form submission came from Credit button or Expense button
        if "Credit" in request.POST or request.POST.get("transaction_type") == "Credit":
            t_type = "CREDIT"
        else:
            t_type = "EXPENSE"

        if amt and date_val:
            Transaction.objects.create(
                transaction_type=t_type,
                amount=amt,
                description=descrip,
                category=cat,
                date=date_val
            )
        return redirect("/")

    # Fetch transactions
    transactions = Transaction.objects.all()
    
    total_income = sum(t.amount for t in transactions if t.transaction_type == "CREDIT") or 0
    total_expense = sum(t.amount for t in transactions if t.transaction_type == "EXPENSE") or 0
    current_balance = total_income - total_expense

    # Category breakdown for expenses
    expense_txs = [t for t in transactions if t.transaction_type == "EXPENSE"]
    category_totals = {}
    for t in expense_txs:
        cat_display = t.category.capitalize()
        category_totals[cat_display] = category_totals.get(cat_display, 0) + float(t.amount)
    
    max_cat_val = max(category_totals.values()) if category_totals else 1
    category_bars = []
    for cat_name, cat_amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True)[:5]:
        percent = min(100, max(5, int((cat_amt / max_cat_val) * 100)))
        category_bars.append({
            "name": cat_name,
            "amount": round(cat_amt, 2),
            "percent": percent
        })

    # Recent transactions
    recent_transactions = transactions[:8]

    # Chart data (Monthly totals for expenses and income - past 12 months)
    today = datetime.date.today()
    months = []
    expense_data = []
    income_data = []

    for i in range(11, -1, -1):
        year = today.year
        month = today.month - i
        while month <= 0:
            month += 12
            year -= 1
        month_name = datetime.date(year, month, 1).strftime("%b")
        months.append(month_name)

        m_exp = sum(float(t.amount) for t in transactions if t.transaction_type == "EXPENSE" and t.date.month == month and t.date.year == year)
        m_inc = sum(float(t.amount) for t in transactions if t.transaction_type == "CREDIT" and t.date.month == month and t.date.year == year)
        expense_data.append(round(m_exp, 2))
        income_data.append(round(m_inc, 2))


    context = {
        "name": user_settings.name.capitalize(),
        "currency": user_settings.currency,
        "total_income": f"{total_income:,.2f}",
        "total_expense": f"{total_expense:,.2f}",
        "current_balance": f"{current_balance:,.2f}",
        "is_negative": current_balance < 0,
        "category_bars": category_bars,
        "recent_transactions": recent_transactions,
        "chart_labels_json": json.dumps(months),
        "chart_expense_json": json.dumps(expense_data),
        "chart_income_json": json.dumps(income_data),
    }

    return render(request, "home.html", context)

def delete_transaction(request, pk):
    if request.method == "POST":
        Transaction.objects.filter(id=pk).delete()
    return redirect("/")
