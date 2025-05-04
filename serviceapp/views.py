from django.shortcuts import render
from .models import Service

# Create your views here.
def service_details(request, service_id):
    service = Service.objects.get(pk=service_id)

    return render(request, "myapp/service-details.html", {'service': service})

