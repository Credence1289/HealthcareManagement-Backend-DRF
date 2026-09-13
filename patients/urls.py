from django.urls import include, path

from .views import PatientListViewSet, PatientDetailView

urlpatterns = [
    path("", PatientListViewSet.as_view()),
    path("<int:pk>/", PatientDetailView.as_view())
]