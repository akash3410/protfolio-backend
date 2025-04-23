from django.contrib import admin
from .models import Education, ProfessionalExperience, Certification

# Register your models here.
admin.site.register(Education)
admin.site.register(ProfessionalExperience)
admin.site.register(Certification)