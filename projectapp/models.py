from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Categorie, related_name='projects')
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

