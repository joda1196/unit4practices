from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def root(request):
    return render(request, "base.html")


def sign_up(request):
    context = {}
    return render(request, "signup.html", {"context": context})


def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("base.html")
        else:
            messages.success(request, ("Please Try Again."))
            return redirect("login")
    return render(request, "login.html")
