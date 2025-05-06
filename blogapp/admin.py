from django.contrib import admin
from .models import Categorie, Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:  # Only set user on creation
            obj.user = request.user
        obj.save()
        
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "categories":
            kwargs["queryset"] = Categorie.objects.filter(is_active=True)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Categorie)