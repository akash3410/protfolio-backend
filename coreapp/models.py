from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    phone = PhoneNumberField(region="BD")
    address = models.TextField()
    website = models.URLField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='profile/')
    date_of_birth = models.DateField()
    degree = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and PersonalInfo.objects.exists():
            raise Exception('There can only be one Personal Info instance!')
        return super().save(*args, **kwargs)
    
    @property
    def age(self):
        today = date.today()
        dob = self.date_of_birth
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    def __str__(self):
        return f"Personal Information for {self.name}"
    
    class Meta:
        verbose_name = "Personal Info"
        verbose_name_plural = "Personal Info"

class About(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    profile_summary = models.TextField(max_length=250)
    profile_summary2 = models.TextField(max_length=500, null=True, blank=True)
    photo = models.ImageField(upload_to='profile/')

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise Exception('There can only be one instance!')
        else:
            return super().save(*args, **kwargs)
        
    def __str__(self):
        return "About"
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

class Social(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=100)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    title = models.CharField(max_length=50)
    progress = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Description(models.Model):
    skill = models.TextField(max_length=200, null=True, blank=True)
    resume = models.TextField(max_length=200, null=True, blank=True)
    projects = models.TextField(max_length=200, null=True, blank=True)
    service = models.TextField(max_length=200, null=True, blank=True)
    testmonial = models.TextField(max_length=200, null=True, blank=True)
    contact = models.TextField(max_length=200, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk and Description.objects.exists():
            raise Exception('There can only be one instance!')
        else:
            return super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Descriptions"