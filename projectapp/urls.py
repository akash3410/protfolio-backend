from django.urls import path
from .import views

urlpatterns = [
    path('<int:project_id>', views.project_details, name="projectDetails"),
    path('review/submit/<int:project_id>/', views.submit_review, name="reviewsubmit")
]