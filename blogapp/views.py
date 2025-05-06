from django.shortcuts import render
from .models import Blog, Categorie

# Create your views here.
def blog_view(request):
    category_id = request.GET.get('category')
    blogs = Blog.objects.filter(is_active=True).order_by("-created_at")
    categories = Categorie.objects.filter(is_active=True)

    if category_id:
        blogs = blogs.filter(categories__id=category_id)

    context = {
        'blogs': blogs,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
    }

    return render(request, "blogapp/blogs.html", context)
