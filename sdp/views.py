import csv
from django.http import *
from django.shortcuts import *
from .models import Article, Caruserinfo
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def login(request):
    return render(request,'LoginPage.html')

def navbar(request):
    return render(request,'Navbar.html')

def login1(request):
    if request.method == 'POST':
        email = request.POST.get('emailinput')  # Using get() method to safely retrieve data
        password = request.POST.get('passwordinput')
        
        try:
            user = Article.objects.get(email=email, password=password) # Authenticate user
        except Article.DoesNotExist:
            user = None
            
        if user is not None:
            # login(user)  # Login the user
            return redirect('home')  # Redirect to home page upon successful login
        else:
            messages.error(request, 'Invalid credentials or user does not exist.')  # Display error message
            return redirect('login')  # Redirect back to login page
    else:
        return render(request, 'LoginPage.html')


# def signup1(req):
#     if req.method=="POST":
#         username=req.POST['name']
#         email=req.POST['email']
#         pass1=req.POST['password']
#         phone=req.POST['phonenumber']


#         user=auth.authenticate(email=email,password=pass1)
#         if user is not None:
#             return render('Home.html')
#         else:
#             user = User.objects.create_user(name=username,email=email,password=pass1,phonenumber=phone)
#             user.save()
#             messages.info('Account is Successfully Created')
#             return render('Home.html')


def signup(request):
    return render(request,'Register.html')

def registerlogin(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        if Article.objects.filter(email=email).exists():
            return HttpResponse("Email is already Registered Please try with another Email")

        Article.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('home')
    return render(request,'Register.html')

def logout(request):
    return redirect('home')

def carbook(request):
    return render(request,'BookCar.html')

def home(request):
    return render(request,'Home.html')

def takerentcar(request):
    return render(request,'Takerentcar.html')

def car1(request):
    return render(request,'car1.html')

def car2(request):
    return render(request,'car2.html')

def car(request):
    return render(request,'car.html')


def car3(request):
    return render(request,'car3.html')

def car4(request):
    return render(request,'car4.html')

def car5(request):
    return render(request,'car5.html')

def car6(request):
    return render(request,'car6.html')

def car7(request):
    return render(request,'car7.html')

def car8(request):
    return render(request,'car8.html')

def car9(request):
    return render(request,'car9.html')

def car10(request):
    return render(request,'car10.html')

def logout(request):
    return redirect('home')

import csv
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .models import Caruserinfo  # Assuming you have a model named Caruserinfo

def book(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')

        if Caruserinfo.objects.filter(email=email).exists():
            return HttpResponse("<h1>Your car had been booked we will update it for you in gmail.<h1>")

        # Creating the Caruserinfo object
        car_user_info = Caruserinfo.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)

        # Sending email to the user
        subject = 'Hello User'  
        message_body = '<h1 text-align:center>you have successfully booked a car<h1>'
        send_mail(
            subject,
            message_body,
            '200030959cseh@gmail.com',
            [email],
            fail_silently=False,
        )
        print(f'Sent email to {email}')

        return HttpResponse("Your car had been booked and an email has been sent to you.")
    return render(request, 'Register.html')

