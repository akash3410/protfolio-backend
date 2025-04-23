from .models import Education, ProfessionalExperience, Certification

def globalEducation(request):
    try:
        educations = Education.objects.all()
    except Education.DoesNotExist:
        educations = None
    return{'educations': educations}

def globalProfessional(request):
    try:
        profexps = ProfessionalExperience.objects.all()
    except ProfessionalExperience.DoesNotExist:
        profexps = None
    return{'profexps': profexps}

def globalCertification(request):
    try:
        certifications = Certification.objects.filter(is_active=True)
    except Certification.DoesNotExist:
        certifications = None
    return{'certifications': certifications}