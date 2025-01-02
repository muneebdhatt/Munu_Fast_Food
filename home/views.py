from django.shortcuts import render, HttpResponse,redirect
from home.models import Contact
from datetime import datetime
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from accounts.views import signup

# Create your views here.

def index(request):
    #return HttpResponse('this is homepage.')
    if request.user.is_anonymous:
        return redirect("login")
    return render(request,"index.html")

def menu(request):
    return render(request,"menu.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if not name or not email or not phone or not desc:
            return HttpResponse("All fields are required.")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        return HttpResponse("Your form has been submitted successfully!")
    #return HttpResponse('this is contact page.')
    return render(request,"contact.html")

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,"login.html")
   
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")