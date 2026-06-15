from django.db import models
from patient.models import Patient
from medecin.models import Medecin
from decimal import Decimal

class Facture(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='factures'
    )
    date = models.DateField(auto_now_add=True)
    medecin = models.ForeignKey(Medecin, related_name="factures", on_delete=models.CASCADE, null=True,blank=True)
    
    payee = models.BooleanField(default=False)
    class Meta:
        ordering=["-date"]
        indexes=[models.Index(fields=['patient', 'payee'])]
    @property    
    def prix_total(self):
        return sum(detail.get_montant() for detail in self.details_facture.all())
        

    def __str__(self):
        return f"Facture {self.patient}"
class DetailFacture(models.Model):
    quantite = models.IntegerField()
    prix = models.DecimalField(max_digits=12, decimal_places=2)
    facture = models.ForeignKey(Facture, related_name='details_facture', on_delete=models.CASCADE)
    medicament = models.CharField(max_length=250)
    def get_montant(self):
    
      try:
        return int(self.quantite) * Decimal(self.prix)
      except:
        return Decimal('0.00')
      


# Create your models here.
