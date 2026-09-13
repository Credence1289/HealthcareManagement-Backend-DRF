from rest_framework import serializers

from mappings.models import PatientDoctorMapping

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = [
            "id", 
            "patient", 
            "doctor", 
            "assigned_at"
        ]

        read_only_fields = ["id", "assigned_at"]
        validators = []
    def validate(self, attrs):
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')

        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError(
                f"This {doctor.name} is already assigned to the {patient.name}."
            )
        return attrs


    def validate_patient(self, patient):
        request = self.context["request"]

        if patient.created_by_id != request.user.id:
            raise serializers.ValidationError(
                "You cannot assign a doctor to another user's patient."
            )

        return patient