from django.contrib import admin
from .models import Paiement

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('facture', 'montant', 'mode_paiement', 'date')
    list_filter = ('mode_paiement', 'date')
# Register your models here.
