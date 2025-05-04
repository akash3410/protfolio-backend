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
    more_info = models.TextField(null=True, blank=True)
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

class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 5)]

    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment