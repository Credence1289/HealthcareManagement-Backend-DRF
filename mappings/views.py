from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

# GET(all), POST
class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        )

# GET all mappings for a specific patient
class MappingPatientView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient_id=self.kwargs["patient_id"],
            patient__created_by=self.request.user,
        )
#DELETE VIEW
class MappingDeleteView(generics.DestroyAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        )