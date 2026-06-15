
from django.db import models

from django.contrib.auth.models import User
from django.conf import settings
from departement.models import Departement
from django.utils import timezone


# =========================
# Patient
# =========================
class Patient(models.Model):
    SEXE_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(blank=True)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    numero_patient = models.CharField(max_length=20, unique=True, blank=True, null=True)
    adresse = models.TextField()
    groupe_sanguin = models.CharField(max_length=5, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    class Meta:
        ordering=['-created_at']
    def save(self, *args, **kwargs):
        is_new = self.id is None
            # Créer un utilisateur associé au patient
            
            
        super().save(*args, **kwargs)
        if is_new: 
            annee = timezone.now().year
            self.numero_patient = f"PAT-{annee}-{self.id:05d}"
            self.save(update_fields=['numero_patient'])
               

        


# Create your models here.
