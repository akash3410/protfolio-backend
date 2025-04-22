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
