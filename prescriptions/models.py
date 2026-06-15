from django.db import models
from consultations.models import Consultation
from patient.models import Patient
from medecin.models import Medecin


class Prescription(models.Model):

    consultation = models.OneToOneField(
        Consultation,
        on_delete=models.CASCADE,
        related_name='prescription'
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )

    medecin = models.ForeignKey(
        Medecin,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )

    date_prescription = models.DateTimeField(
        auto_now_add=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )
    class Meta:
        verbose_name = "Prescription"
        verbose_name_plural = "Prescriptions"
        indexes = [
            models.Index(fields=['date_prescription']),
            models.Index(fields=['patient']),

        ]
        ordering = ['-date_prescription']

    def __str__(self):

        return f"Prescription #{self.id} - {self.patient}"

class ItemsPrescription(models.Model):

    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        related_name='lignes'
    )

    medicament = models.CharField(
        max_length=255
    )

    dosage = models.CharField(
        max_length=100
    )

    frequence = models.CharField(
        max_length=100
    )

    duree = models.CharField(
        max_length=100
    )

    quantite = models.PositiveIntegerField()

    instructions = models.TextField(
        blank=True,
        null=True
    )
    class Meta:
        indexes= [
            models.Index(fields=['prescription']),
        ]

    def __str__(self):

        return self.medicament    

# Create your models here.
