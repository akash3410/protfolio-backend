from django.contrib import admin
from .models import ContactMessage, Role

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj = ...):
        return True
    
    def get_readonly_fields(self, request, obj = ...):
        if obj:
            return [f.name for f in self.model._meta.fields if f.name not in ['responed', 'is_read']]
        return []
    
    list_display = ['name', 'email', 'is_read', 'responed', 'created_at']
    list_filter = ['is_read', 'responed']
    search_fields = ['name', 'emai', 'message']

admin.site.register(Role)