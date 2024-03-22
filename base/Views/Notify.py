from django.shortcuts import render, redirect
from base.models import Notification
from django.utils import timezone

def add_notification(request):
    datas = Notification.objects.filter(user=request.user).order_by('-last_updated_time')
    if request.method == 'POST':
        notify_time = request.POST.get('notify_time')
        tablet_name = request.POST.get('tablet_name')
        quantity = request.POST.get('quantity')
        total_tablet_quantity = request.POST.get('total_tablet_quantity')

        # Create a new Notification object and save it to the database
        Notification.objects.create(
            user=request.user,
            notify_time=notify_time,
            tablet_name=tablet_name,
            quantity=quantity,
            total_tablet_quantity=total_tablet_quantity,
            last_updated_time=timezone.now()
        )
        
        return redirect('notification_list')  # Redirect to notification list view
    return render(request, 'Notify/add_notification.html', {'datas':datas})
