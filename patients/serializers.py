from rest_framework import serializers

from patients.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "age",
            "gender",
            "phone_number",
            "address",
            "illness",
            "medical_notes",
            "created_by",
            "created_at",
            "updated_at",            
        ]
        read_only_fields = ["created_by", "created_at", "updated_at"]

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError('Age must be greater than 0.')
        return value