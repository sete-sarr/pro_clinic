from django.contrib import admin
from .models import Consultation

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medecin', 'date')
    list_filter = ('date',)
    search_fields = ('patient__nom', 'medecin__user__username')
# Register your models here.
