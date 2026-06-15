from django.contrib import admin
from .models import Departement
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)

# Register your models here.
