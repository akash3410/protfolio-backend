from django.urls import path
from .import views

urlpatterns = [
    path('review/submit/<int:project_id>/', views.submit_review, name="reviewsubmit")
]