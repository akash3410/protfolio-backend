from django.http import FileResponse, Http404
from django.shortcuts import render
from .models import Resume

# Create your views here.
def download_cv(request):
    try:
        pdf = Resume.objects.get()
        return FileResponse(open(pdf.cv.path, 'rb'), content_type='application/pdf')
    except Resume.DoesNotExist:
        raise Http404("No PDF uploaded yet!")
