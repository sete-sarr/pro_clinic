from django.contrib import admin

from .models import Facture, DetailFacture

class DetailFactureAdmin(admin.TabularInline):
  model=DetailFacture
@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('patient',  'payee', 'date')
    list_filter = ('payee', 'date')
    search_fields = ('patient__nom',)
    inlines=[DetailFactureAdmin]



# Register your models here.
