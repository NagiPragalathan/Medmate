# yourapp/management/commands/notify_users.py

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from base.models import Notification

class Command(BaseCommand):
    help = 'Send notification emails to users based on notify_time'

    def handle(self, *args, **kwargs):
        notifications = Notification.objects.filter(notify_time__date=timezone.now().date())

        for notification in notifications:
            subject = f'Notification for {notification.user.username}'
            message = f"Hello {notification.user.username},\n\nYour notification for {notification.tablet_name} is due today."
            send_mail(subject, message, 'your@example.com', [notification.user.email])

        self.stdout.write(self.style.SUCCESS('Notification emails sent successfully.'))
