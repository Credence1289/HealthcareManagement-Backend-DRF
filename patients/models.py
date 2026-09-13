from django.conf import settings
from django.db import models


class Patient(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patients"
    )
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=10,
        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
    )
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    illness = models.CharField(max_length=200, blank=True, null=True)
    medical_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
