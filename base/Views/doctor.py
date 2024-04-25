from django.shortcuts import render
from django.contrib.auth.models import User
from base.models import UserRole, UserProfile

def DoctorList(request):
    usr_obj = UserRole.objects.filter(role='doctor')
    users = []
    for i in usr_obj:
        user_temp = User.objects.get(id=i.user.id)
        user_temp.profile = UserProfile(user=user_temp)
        users.append(user_temp)
        print(i.user, i.role, i)
    print(users)
    return render(request, 'doctor/list-Doctor.html', { "doctors" : users })
