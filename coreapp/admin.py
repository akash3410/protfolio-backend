from django.contrib import admin
from .models import PersonalInfo

# Register your models here.
admin.site.site_header = "My Administration"
admin.site.site_title = "Admin"
admin.site.index_title = "Dashboard"

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not PersonalInfo.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False