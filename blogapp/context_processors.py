from .models import Blog

def blogCount_context(request):
    total_blogs = Blog.objects.count()
    return {'total_blog': total_blogs}