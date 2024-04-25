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



class UserProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey field for the User model
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # ForeignKey field for the Product model
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.product_name}"

class UserDocuments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document_name = models.CharField(max_length=255)
    document = models.FileField(upload_to='user_documents/')
    ipfs_id = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_name

class CareTaker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey field for the User model
    name = models.CharField(max_length=100)
    mailId = models.EmailField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    change_profile = models.ImageField(upload_to='profiles/', blank=True, null=True)
    background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    address_street = models.CharField(max_length=255, blank=True, null=True)
    address_city = models.CharField(max_length=100, blank=True, null=True)
    address_state = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
   
    biography = models.TextField(blank=True, null=True)
    experience = models.FileField(upload_to='experiences/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.email}"