from django.contrib import admin

from .models import Patient
    



@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'telephone', 'sexe', 'date_naissance', 'groupe_sanguin','email', 'numero_patient')
    search_fields = ('prenom', 'nom', 'telephone')
    list_filter = ('sexe',)

# Register your models here.
