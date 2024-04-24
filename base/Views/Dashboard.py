from django.shortcuts import render
from base.models import Notification


def dash(request):
    return render(request, 'baseindex/index.html')
def prescription(request):
    return render(request, 'Ecommerce/prescription.html')
def report(request):
    return render(request, 'Ecommerce/report.html')
def viewprescription(request):
    return render(request,'Ecommerce/viewprescription.html')
def viewreport(request):
    return render(request,'Ecommerce/viewreport.html')
def Addprescription(request):
    return render(request,'Ecommerce/Add-prescription.html')
def Addreport(request):
    return render(request,'Ecommerce/Add-report.html')

