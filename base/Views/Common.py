# views.py
from django.shortcuts import render
from base.models import Notification

def home(request):
    alarm = Notification(user=request.user)
    return render(request, 'Home/index.html', {"userTime":alarm})
