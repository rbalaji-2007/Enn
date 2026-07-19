from django.shortcuts import render

# Create your views here.
def home(request):
    name = "vedant".capitalize()
    return render(
        request, 
        "home.html", 
        {"name": name}
        )

