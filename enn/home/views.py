from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request, 
        "home/home.html", 
        {"name": "Ved", "balance": "65,906", "income":"8,654", "expense": "6,547"}
        )

