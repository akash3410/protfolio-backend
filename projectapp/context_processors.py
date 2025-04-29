from .models import Project

def globalProject(request):
    try:
        projects = Project.objects.filter(status=True)
    except Project.DoesNotExist:
        projects = None
    return{'projects': projects}