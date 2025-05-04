from .models import PersonalInfo, About, Social, Skill, Description

def global_personal_info(request):
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        info = None
    return {'personal_info': personal_info}

def global_about(request):
    try:
        about = About.objects.first()
    except About.DoesNotExist:
        about = None
    return {'about': about}

def globalSocial(request):
    try:
        socials = Social.objects.filter(is_active=True)
    except Social.DoesNotExist:
        socials = None
    return{'socials': socials}

def globalSkill(request):
    try:
        skills = Skill.objects.filter(is_active=True)
    except Skill.DoesNotExist:
        skills = None
    return{'skills': skills}

def global_description(request):
    try:
        description = Description.objects.first()
    except Description.DoesNotExist:
        description = None
    return {'description': description}