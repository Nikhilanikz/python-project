from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pasword = request.POST['password']
        user = auth.authenticate(username=username, password=pasword)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        firstname = request.POST['First_name']
        lastname = request.POST['Last_name']
        email = request.POST['Email']
        password = request.POST['Password']
        cpassword = request.POST['ConformPassword']
        if password == cpassword:
            if User.objects. filter(username=username).exists():
                messages.info(request, "Username already Taken")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "email already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

