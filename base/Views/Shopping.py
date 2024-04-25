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

def testimonial(request):
     return render(request,'Buy_medicines/testimonial.html')

def chackout(request):
     return render(request,'Buy_medicines/chackout.html')

def error(request):
     return render(request,'Buy_medicines/404.html')

def contact(request):
     return render(request,'Buy_medicines/contact.html')

def documents(request):
     return render(request,'medical/documents.html')
