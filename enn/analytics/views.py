from django.shortcuts import render
from home.models import Transaction, UserSettings
import datetime
import json

def analytics(request):
    user_settings = UserSettings.get_settings()
    transactions = Transaction.objects.all()
    
    expense_txs = [t for t in transactions if t.transaction_type == "EXPENSE"]
    category_totals = {}
    for t in expense_txs:
        cat_display = t.category.capitalize()
        category_totals[cat_display] = category_totals.get(cat_display, 0) + float(t.amount)

    max_cat_val = max(category_totals.values()) if category_totals else 1

    category_bars = []
    for cat_name, cat_amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        percent = min(100, max(5, int((cat_amt / max_cat_val) * 100)))
        category_bars.append({
            "name": cat_name,
            "amount": f"{cat_amt:,.2f}",
            "percent": percent
        })

    # Prepare past 12 calendar months
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
        "currency": user_settings.currency,
        "category_bars": category_bars,
        "chart_labels_json": json.dumps(months),
        "chart_expense_json": json.dumps(expense_data),
        "chart_income_json": json.dumps(income_data),
    }

    return render(request, "analytics.html", context)
