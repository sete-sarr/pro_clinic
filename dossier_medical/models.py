from django.db import models
from patient.models import Patient



class DossierMedical(models.Model):
    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        related_name='dossier_medical'
    )
    allergies = models.TextField(blank=True)
    antecedents = models.TextField(blank=True)
    observations = models.TextField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dossier médical - {self.patient}"

# Create your models here.
