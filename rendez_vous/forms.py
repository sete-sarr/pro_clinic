from django import forms
from .models import RendezVous

class RendezVousForm(forms.ModelForm):


    class Meta:
        model = RendezVous
        fields=['patient','date', 'heure', 'statut']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control select2'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'heure': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),  
        }