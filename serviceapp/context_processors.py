from .models import Service

def globalService(request):
    try:
        services = Service.objects.filter(is_active=True)
    except Service.DoesNotExist:
        services = None
    return{'services': services}