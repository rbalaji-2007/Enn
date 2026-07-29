from django.shortcuts import render, redirect
from home.models import Transaction, UserSettings

def setting(request):
    user_settings = UserSettings.get_settings()
    
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "save":
            new_name = request.POST.get("name", "").strip()
            if new_name:
                user_settings.name = new_name
                user_settings.save()
        elif action == "reset":
            Transaction.objects.all().delete()
        return redirect("/settings")

    context = {
        "name": user_settings.name,
        "currency": user_settings.currency,
    }
    return render(request, "settings.html", context)
