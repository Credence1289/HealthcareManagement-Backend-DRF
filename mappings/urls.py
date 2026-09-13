from django.urls import path
from .views import MappingListCreateView, MappingPatientView, MappingDeleteView

urlpatterns = [
    path("", MappingListCreateView.as_view()),
    path("<int:patient_id>/", MappingPatientView.as_view()),
    path("<int:pk>/delete/", MappingDeleteView.as_view()),
]