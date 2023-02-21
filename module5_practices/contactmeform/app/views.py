from django.shortcuts import render, redirect
from app.forms import ContactForm
from django.http import HttpResponse

# Create your views here.
def contact(request):
    form = ContactForm(request.GET)
    if form.is_valid():
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        context = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "message": message,
        }
        return render(request, "base.html", context)
    else:
        return render(request, "base.html")
