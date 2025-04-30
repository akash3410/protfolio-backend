from .models import Project, Review

def globalProject(request):
    try:
        projects = Project.objects.all()
    except Project.DoesNotExist:
        projects = None
    return{'projects': projects}

def globalReview(request):
    try:
        reviews = Review.objects.all()
    except Review.DoesNotExist:
        reviews = None
    return{'reviews': reviews}