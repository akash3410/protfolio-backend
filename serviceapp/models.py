from django.db import models

# Create your models here.
class Categorie(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    more_info = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Categorie, related_name='services')
    features = models.ManyToManyField(Feature, related_name='services')
    icon = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
