from .models import Education

def globalEducation(request):
    try:
        educations = Education.objects.all()
    except Education.DoesNotExist:
        educations = None
    return{'educations': educations}