from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.timezone import now
from gridfs import GridFS
from pymongo import MongoClient



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
    
class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey field for the User model
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)


class DoctorConsultRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_requests')
    patient_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_requests')
    time = models.DateTimeField()
    message = models.TextField()
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class DoctorRating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor_usr_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_given')
    usrid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_received')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rating for Doctor {self.doctor_usr_id.username} by {self.usrid.username}: {self.rating}"

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
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


    
class EProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product/', blank=True, null=True)
    description = models.CharField(max_length=200)
    product_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_added_date = models.DateTimeField(default=now)  # Automatically sets the field to now

    def __str__(self):
        return self.product_name
    
class PatientDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_gridfs_id = models.CharField(max_length=255, blank=True)
    file_content = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    last_updated_file = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Document ID: {self.id}, User: {self.user.username}"