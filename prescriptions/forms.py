from django import forms
from django.forms.models import inlineformset_factory
from .models import Prescription, ItemsPrescription
from django.forms.models import ModelForm

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['consultation','patient', 'notes']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            
            'consultation': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  
        }
PrescriptionFormset = inlineformset_factory(
    Prescription, ItemsPrescription, fields=('medicament', 'dosage', 'frequence', 'duree', 'quantite','instructions'), widgets={'medicament': forms.TextInput(attrs={'class': 'form-control'}), 'dosage': forms.TextInput(attrs={'class': 'form-control'}), 'frequence': forms.TextInput(attrs={'class': 'form-control'}), 'duree': forms.TextInput(attrs={'class': 'form-control'}), 'quantite': forms.NumberInput(attrs={'class': 'form-control'}), 'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 2})}, extra=5, can_delete=True
)