from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import Userreg


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("i am here")
            # does nothing, just trigger the validation
            return render(request, 'loggedin.html', {"username": form.cleaned_data.get('name')})
    else:
        form = ContactForm()
        return render(request, 'home.html', {'form': form})

def AuthenticateUser(emailID, passwd):
    users = Userreg.objects.all()
    print(users)
    q = users.filter(EmailID=emailID, Password=passwd)
    
    if q :
        return True
    else :
        return False

def login(request):
    username = "not logged in"
    if request.method == "POST":
        # Get the posted form
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data.get('username')
            if AuthenticateUser(loginForm.cleaned_data.get('username'),loginForm.cleaned_data.get('Password')):
                return render(request, 'loggedin.html', {"username": username})
            else:
                return render(request, 'login.html', {'messages':'Login Failed, Please try again', 'loginForm': loginForm})
    else:
        loginForm = LoginForm()
    return render(request, 'login.html', {'loginForm': loginForm})


def userRegistration(request):
    if request.method == "POST":
        registerForm = UserRegistrationForm(request.POST)
        if registerForm.is_valid():
            user = Userreg()
            user.FirstName = registerForm.cleaned_data.get('FirstName')
            user.LastName = registerForm.cleaned_data.get('LastName')
            user.Password = registerForm.cleaned_data.get('Password')
            user.EmailID = registerForm.cleaned_data.get('EmailID')
            user.MobileNo = registerForm.cleaned_data.get('MobileNo')
            user.MaritalStatus = registerForm.cleaned_data.get('MaritalStatus')
            user.Gender = registerForm.cleaned_data.get('Gender')
            user.DOB = registerForm.cleaned_data.get('DOB')
            user.save()
            return render(request, 'registration.html', {'messages': {user.FirstName, user.LastName, 'registered successfully'}, 'registerForm': registerForm})
    else:
       registerForm = UserRegistrationForm()
       print("I am here to display register page")
    return  render(request, 'registration.html', { 'registerForm': registerForm })
