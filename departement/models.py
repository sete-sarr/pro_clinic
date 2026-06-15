from django.db import models

class Departement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField( blank=True, null=True)
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name = "Département"
        verbose_name_plural = "Départements"
        ordering = ['nom']
        indexes = [
            models.Index(fields=['nom']),
            
        ]

# Create your models here.
