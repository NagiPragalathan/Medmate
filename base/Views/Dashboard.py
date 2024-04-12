from django.shortcuts import render
from base.models import Notification

def dash(request):
    return render(request, 'Ecommerce/index.html')
