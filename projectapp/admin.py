from django.contrib import admin
from .models import Categorie, Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('client', 'title', 'description', 'link', 'image', 'deadline', 'file', 'status')

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

admin.site.register(Categorie)
admin.site.register(Project ,ProjectAdmin)

