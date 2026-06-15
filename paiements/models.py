from django.db import models

from facturations.models import Facture
class Paiement(models.Model):
    MODE_PAIEMENT_CHOICES = (
        ('cash', 'Espèces'),
        ('mobile', 'Mobile Money'),
        ('carte', 'Carte bancaire'),
    )

    facture = models.ForeignKey(
        Facture,
        on_delete=models.CASCADE,
        related_name='paiements'
    )
    date = models.DateField(auto_now_add=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    mode_paiement = models.CharField(
        max_length=20,
        choices=MODE_PAIEMENT_CHOICES
    )

    def __str__(self):
        return f"Paiement {self.montant} - {self.mode_paiement}"

# Create your models here.
