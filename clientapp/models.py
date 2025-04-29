from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ClientInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='clientinfo')
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=150, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = PhoneNumberField(region="BD", null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    cover_photo = models.ImageField(upload_to='client/', null=True, blank=True)
    profile_photo = models.ImageField(upload_to='client/', null=True, blank=True)

    def __str__(self):
        return self.full_name