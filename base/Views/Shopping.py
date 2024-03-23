# views.py
from django.shortcuts import render
from base.models import Product

def Shoppingview(request):
    alarm = Product.objects.all()
    return render(request, 'medical/medshopping.html', {"products":alarm})
