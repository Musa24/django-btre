from django.shortcuts import render ,redirect
from django.contrib import messages



def register(request):
    if request.method == "POST":
        messages.error(request,"Testing error message")
        return redirect("register")
    else:
        return render(request, "accounts/register.html")

def login(request):
    
    return render(request, "accounts/login.html")

def logout(request):
    pass


def dashboard(request):
    return render(request, "accounts/dashboard.html")