from django.contrib import admin
from .models import DossierMedical


@admin.register(DossierMedical)
class DossierMedicalAdmin(admin.ModelAdmin):
    list_display = ('patient',)
    search_fields = ('patient__nom',)
