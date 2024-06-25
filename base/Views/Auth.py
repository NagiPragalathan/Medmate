# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from base.models import UserRole
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            return render(request, 'Auth/login.html', {'error': 'Invalid username or password'})
    return render(request, 'Auth/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST.get('userType')
        print(username, password)
        user = User.objects.create_user(username=username, password=password)
        user_Role = UserRole(user=user, role=user_type)
        user_Role.save()
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful signup
        else:
            return render(request, 'Auth/signup.html', {'error': 'Signup failed'})
    return render(request, 'Auth/signup.html')


# views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

