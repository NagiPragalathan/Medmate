from django.shortcuts import render, redirect
from base.models import Notification

def add_notification(request):
    if request.method == 'POST':
        return render(request, 'add_notification.html')
