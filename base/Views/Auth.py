# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('home')  # Redirect to home page after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'Auth/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('home')  # Redirect to home page after successful signup
        else:
            return render(request, 'signup.html', {'error': 'Signup failed'})
    return render(request, 'Auth/signup.html')
