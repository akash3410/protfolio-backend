from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    responed = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    resopned_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
