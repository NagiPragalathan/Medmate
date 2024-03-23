from django.shortcuts import render, redirect,get_object_or_404
from base.models import CareTaker

def add_caretaker(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mailId = request.POST.get('mailId')
        caretaker = CareTaker(name=name,user=request.user, mailId=mailId)
        caretaker.save()
        return redirect('caretaker_list')
    return render(request, 'CareTaker/add_caretaker.html')

def caretaker_list(request):
    caretakers = CareTaker.objects.all()
    return render(request, 'CareTaker/caretaker_list.html', {'caretakers': caretakers})

def caretaker_edit(request, caretaker_id):
    caretaker = get_object_or_404(CareTaker, id=caretaker_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        mailId = request.POST.get('mailId')
        # Update the CareTaker object with the new data
        caretaker.name = name
        caretaker.mailId = mailId
        caretaker.save()
        return redirect('caretaker_list')
    return render(request, 'CareTaker/caretaker_edit.html', {'caretaker': caretaker})


def caretaker_delete(request, caretaker_id):
    caretaker = get_object_or_404(CareTaker, id=caretaker_id)
    if request.method == 'GET':
        caretaker.delete()
        return redirect('caretaker_list')
    return render(request, 'CareTaker/caretaker_delete.html', {'caretaker': caretaker})
