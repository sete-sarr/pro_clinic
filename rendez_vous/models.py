from django.db import models
from medecin.models import Medecin
from patient.models import Patient


class RendezVous(models.Model):
    STATUT_CHOICES = (
        ('attente', 'En attente'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='rendez_vous'
    )
    medecin = models.ForeignKey(
        Medecin,
        on_delete=models.CASCADE,
        related_name='rendez_vous'
    )
    date = models.DateTimeField()
    heure = models.TimeField()
    statut = models.CharField(
        max_length=10,
        choices=STATUT_CHOICES,
        default='attente'
    )
    notification_envoyee = models.BooleanField(default=False)

    

    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date', '-heure']
        indexes = [
            models.Index(fields=['date']),      
            models.Index(fields=['medecin']),
            models.Index(fields=['patient']),
        ]
    def __str__(self):
        return f"{self.patient} - {self.date} {self.heure}"

# Create your models here.
