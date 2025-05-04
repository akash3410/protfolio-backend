from django.shortcuts import get_object_or_404, redirect, render
from .models import Project
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def submit_review(request, project_id):
    user = request.user
    project = get_object_or_404(Project, id=project_id)

    # Only allow review if the project belongs to the logged-in client
    if project.client != user:
        return HttpResponseForbidden("You are not allowed to review this project.")
    
    # Prevent double review
    if hasattr(project, 'review'):
        return HttpResponseForbidden("This project already has a review.")

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project  # Set project manually
            review.user = user
            review.save()
            return redirect('profile')
    else:
        form = ReviewForm()

    return render(request, 'projectapp/submit_review.html', {'form': form})

def project_details(request, project_id):
    project = Project.objects.get(pk=project_id)
    
    return render(request, "myapp/project-details.html", {'project': project})