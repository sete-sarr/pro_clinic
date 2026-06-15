from django.db import models
from departement.models import Departement
from django.conf import settings
# =========================
class Medecin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True, blank=True)
    telephone = models.CharField(max_length=20)
    nom = models.CharField(max_length=20, null=True, blank=True)
    prenom = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}" if self.prenom and self.nom else self.user.get_full_name() or self.user.username

# Create your models here.
