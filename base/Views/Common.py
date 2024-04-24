# views.py
from django.shortcuts import render
from base.models import Notification

def home(request):
    try:
        alarm = Notification.objects.filter(user=request.user)[::-1][0]
    except:
        alarm = None
    return render(request, 'Buy_medicines/index.html', {"userTime":alarm})
