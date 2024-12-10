from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import CustomUser

def SignupUser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, "Email already registered.")
            return redirect('login')
        
        newuser = CustomUser.objects.create(name=name, email=email)
        newuser.set_password(password) 
        newuser.save()

        messages.success(request, "User created successfully.")
        return redirect('login')

    return render(request, 'signup.html')



def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        usertologin = authenticate(request, email=email, password=password) 
        if usertologin is not None:
            login(request, usertologin)
            return redirect('home')
        else:
            if not CustomUser.objects.filter(email=email).exists():
                messages.info(request, "Email not Registered")
                return redirect('signup')
            else:
                messages.error(request, "Incorrect Password")
                return redirect('login')
    
    return render(request, 'login.html')


def resetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password changed successfully')
            return redirect('login') 
        except CustomUser.DoesNotExist:
            messages.error(request, 'Email not registered')
            return redirect('signup')
    
    return render(request, 'forgotpassword.html')


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'You have logged out successfully')
        return redirect('login')
    else:
        return redirect('login')