from rest_framework import serializers

from doctors.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "specialization",
            "phone_number",
            "email",
            "experience_years",
            "created_at",
            "updated_at",            
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate_specialization(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('Specialization is required.')
        return value.strip()