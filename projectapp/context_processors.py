from .models import Project, Review, Categorie

def globalProject(request):
    try:
        category_id = request.GET.get('category')
        projects = Project.objects.filter(status=True)
        categories = Categorie.objects.filter(is_active=True)

        if category_id:
            projects = projects.filter(category__id=category_id)
    except Project.DoesNotExist:
        projects = None
    return{
        'projects': projects,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
    }

def globalReview(request):
    try:
        reviews = Review.objects.all()
    except Review.DoesNotExist:
        reviews = None
    return{'reviews': reviews}