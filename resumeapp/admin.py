from django.contrib import admin
from .models import Education, ProfessionalExperience, Certification, Resume

# Register your models here.
admin.site.register(Education)
admin.site.register(ProfessionalExperience)
admin.site.register(Certification)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Resume.objects.exists():
            return False
        return super().has_add_permission(request)