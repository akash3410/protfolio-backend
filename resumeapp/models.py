from django.db import models

# Create your models here.
class Education(models.Model):
    degree = models.CharField(max_length=80)
    institute = models.CharField(max_length=100)
    description = models.TextField()
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.degree
    
class ProfessionalExperience(models.Model):
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    description = models.TextField()
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.designation} at {self.company}"
    
class Certification(models.Model):
    title = models.CharField(max_length=150)
    institute = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    result = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} in {self.institute}"
