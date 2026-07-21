from django.shortcuts import render, redirect

# Create your views here.
def home(request):

    name = "vedant".capitalize()
    if request.method == "POST":
        printData(request)
        return redirect("/")
    
    return render(
        request, 
        "home.html", 
        {"name": name}
        )

def printData(data):
    amt = data.POST["amount"]
    descrip = data.POST["descrip"]
    cat = data.POST["category"]
    date = data.POST["date"]
    if data.POST.get("Credit"):
        print(amt, descrip, cat, date, "credit")
    else:
        print(amt, descrip, cat, date, "expense")
