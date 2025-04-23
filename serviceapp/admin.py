from django.contrib import admin
from .models import Categorie, Feature, Service

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Feature)
admin.site.register(Service)