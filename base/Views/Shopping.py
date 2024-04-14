# views.py
from django.shortcuts import render
from base.models import Product

def Shoppingview(request):
    alarm = Product.objects.all()
    return render(request, 'medical/medshopping.html', {"products":alarm})

def buymed(request):
     return render(request, 'Buy_medicines/index.html')

def medicine(request):
     return render(request,'Buy_medicines/medicine.html')

def cart(request):
     return render(request,'Buy_medicines/cart.html')
