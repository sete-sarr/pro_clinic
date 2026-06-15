import django_filters
from .models import Patient

class PatientFilterset(django_filters.FilterSet):
    prenom = django_filters.CharFilter(field_name='prenom', label='prenom', lookup_expr='icontains')

    nom = django_filters.CharFilter(field_name='nom', label='nom', lookup_expr='icontains')
    telephone = django_filters.CharFilter(field_name='telephone', label='telephone', lookup_expr='iexact')
    class Meta:
        model = Patient
        fields=['prenom', 'nom', 'telephone']