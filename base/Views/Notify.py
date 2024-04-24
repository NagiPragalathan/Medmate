from django.shortcuts import render, redirect, get_object_or_404
from base.models import Notification, CareTaker
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.core.mail import send_mail


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

def notification(request):
    try:
        datas = Notification.objects.filter(user=request.user).latest('notify_time')
    except:
        datas = None
    if datas == None:
        return render(request, 'Notify/notification.html', {'datas':datas})
    datas = Notification.objects.filter(user=request.user).latest('notify_time')
    print(datas)
    medicines_left = int(datas.total_tablet_quantity) - int(datas.quantity)
    days_left = int(int(datas.total_tablet_quantity)/int(datas.quantity))  # Calculate days left to buy medicines
    list_user = []
    care = CareTaker.objects.filter(user=request.user)
    for i in care:
        list_user.append(str(i.mailId))
    subject = 'Time to Take Your Medicines'
    message = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            h1 {{ color: #333; }}
            p {{ margin-bottom: 10px; }}
        </style>
    </head>
    <body>
        <h1>{subject}</h1>
        <p><strong>Medicines Left:</strong> {medicines_left}</p>
        <p><strong>Days Left to Buy Medicines:</strong> {days_left}</p>
        <p><strong>Notify Time:</strong> {datas.notify_time}</p>
        <p><strong>Tablet Name:</strong> {datas.tablet_name}</p>
        <p><strong>Quantity:</strong> {datas.quantity}</p>
    </body>
    </html>
    """
    print(message, request.user.email)
    
    from_email = 'sitejec@gmail.com'
    recipient_list = ['nagipragalathan@gmail.com', request.user.email]
    recipient_list.extend(list_user)
    print(recipient_list)
    send_mail(subject, '', from_email, recipient_list, fail_silently=False, html_message=message)
    print("mail sent successfully..!")

    return render(request, 'Notify/Notification.html', {'datas': datas, 'msg':f'''<h1>{subject}</h1>
        <p><strong>Medicines Left:</strong> {medicines_left}</p>
        <p><strong>Days Left to Buy Medicines:</strong> {days_left}</p>
        <p><strong>Notify Time:</strong> {datas.notify_time}</p>
        <p><strong>Tablet Name:</strong> {datas.tablet_name}</p>
        <p><strong>Quantity:</strong> {datas.quantity}</p>'''})


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

def rating(request):
        return render(request, 'Rating/rating.html')
