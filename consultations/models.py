from django.db import models

from django.utils import timezone
from medecin.models import Medecin
from patient.models import Patient



class Consultation(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='consultations'
    )
    medecin = models.ForeignKey(
        Medecin,
        on_delete=models.CASCADE,
        related_name='consultations'
    )
    date = models.DateTimeField(default=timezone.now)
    diagnostic = models.TextField()
    traitement = models.TextField()
    class Meta:
        ordering=['-date']

    def __str__(self):
        return f"Consultation {self.patient} - {self.date.strftime('%d/%m/%Y')}"
# Create your models here.
