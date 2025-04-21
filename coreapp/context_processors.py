from .models import PersonalInfo

def global_personal_info(request):
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        info = None
    return {'personal_info': personal_info}