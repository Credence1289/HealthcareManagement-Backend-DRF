from django.db import models

from doctors.models import Doctor
from patients.models import Patient

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("patient", "doctor")

    def __str__(self):
        return  f"{self.patient_id} -> {self.doctor_id}"