from django.contrib import admin

from .models import (
    Prescription,
    ItemsPrescription
)


class ItemsPrescriptionInline(admin.TabularInline):

    model = ItemsPrescription

    extra = 1

    fields = (
        'medicament',
        'dosage',
        'frequence',
        'duree',
        'quantite',
        'instructions'
    )


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'patient',
        'medecin',
        'consultation',
        'date_prescription'
    )

    list_filter = (
        'date_prescription',
        'medecin'
    )

    search_fields = (
        'patient__nom',
        'patient__prenom',
        'medecin__nom',
        'medecin__prenom'
    )

    ordering = (
        '-date_prescription',
    )

    inlines = [
        ItemsPrescriptionInline
    ]


@admin.register(ItemsPrescription)
class ItemsPrescriptionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'prescription',
        'medicament',
        'dosage',
        'frequence',
        'duree',
        'quantite'
    )

    search_fields = (
        'medicament',
    )

    list_filter = (
        'medicament',
    )

# Register your models here.
