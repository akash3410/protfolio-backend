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