from .models import Role
import json

def global_role(request):
    try:
        typed_roles = list(Role.objects.values_list('name', flat=True))
    except Role.DoesNotExist:
        typed_roles = None
    return {'typed_roles': typed_roles}