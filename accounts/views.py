from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been created successfully!")
            return redirect('login')
        else:
             print(form.errors)
        return render(request,'signup.html',{'form':form})
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})