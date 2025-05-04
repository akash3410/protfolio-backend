from django.contrib import admin
from .models import PersonalInfo, About, Social, Skill, Description
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

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not About.objects.exists()
    
    def has_delete_permission(self, requset, obj=None):
        return False
    
admin.site.register(Social)

admin.site.register(Skill)

@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Description.objects.exists()
    
    def has_delete_permission(self, requset, obj=None):
        return False