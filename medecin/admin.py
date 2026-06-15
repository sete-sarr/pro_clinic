from django.contrib import admin
from .models import Medecin

@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialite', 'telephone')
    search_fields = ('user__username', 'specialite')

# Register your models here.
