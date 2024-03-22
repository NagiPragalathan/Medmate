from django.db import models
from django.contrib.auth.models import User
import uuid

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notify_time = models.DateTimeField()
    tablet_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    total_tablet_quantity = models.PositiveIntegerField()
    last_updated_time = models.DateTimeField()


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/')
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name