from django.shortcuts import render
from django.contrib.auth.models import User
from base.models import UserRole

def DoctorList(request):
    usr_obj = UserRole.objects.filter(role='doctor')
    users = []
    for i in usr_obj:
        users.append(User.objects.get(id=i.user.id))
        print(i.user, i.role, i)
    print(users)
    return render(request, 'doctor/list-Doctor.html')
