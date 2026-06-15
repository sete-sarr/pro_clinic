# consultation/forms.py
from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = [ 'diagnostic', 'traitement', 'patient']
        widgets = {
            'diagnostic': forms.Textarea(attrs={'rows': 3}),
            'traitement': forms.Textarea(attrs={'rows': 3}),
        }
