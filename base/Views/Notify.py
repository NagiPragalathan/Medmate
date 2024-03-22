from django.shortcuts import render, redirect, get_object_or_404
from base.models import Notification
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

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

        return redirect('add_notify')  # Redirect to notification list view
    return render(request, 'Notify/add_notification.html', {'datas':datas})


@login_required
def delete_notification(request, notification_id):
    if request.method == 'GET':
        try:
            notification = Notification.objects.get(id=notification_id)
            notification.delete()
            return redirect('add_notify')  # Redirect to notification list view after deletion
        except Notification.DoesNotExist:
            return HttpResponseBadRequest("Notification does not exist.")
    else:
        return HttpResponseBadRequest("Invalid request method.")
    
@login_required
def edit_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)

    if request.method == 'POST':
        # Retrieve form data from request
        notify_time = request.POST.get('notify_time')
        tablet_name = request.POST.get('tablet_name')
        quantity = request.POST.get('quantity')
        total_tablet_quantity = request.POST.get('total_tablet_quantity')

        # Update notification object
        notification.notify_time = notify_time
        notification.tablet_name = tablet_name
        notification.quantity = quantity
        notification.total_tablet_quantity = total_tablet_quantity
        notification.save()

        return redirect('add_notify')  # Redirect to notification list view

    return render(request, 'Notify/edit_notification.html', {'notification': notification})