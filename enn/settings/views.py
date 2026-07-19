from django.shortcuts import render

def setting(request):
    return render(request, "settings.html")
