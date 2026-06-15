import django_filters 
from prescriptions.models import Prescription
class PrescriptionFilterSet(django_filters.FilterSet):

    medecin = django_filters.CharFilter(
        field_name='medecin__prenom',
        lookup_expr='icontains'
        )
    date_du = django_filters.DateFilter(
        field_name='date_prescription',
          lookup_expr='gte'
          )
    date_au = django_filters.DateFilter(
        field_name='date_prescription',
        lookup_expr='lte'
        )
    date = django_filters.DateFilter(
        field_name='date_prescription',
        lookup_expr='iexact'
        )
    departement = django_filters.CharFilter(
        field_name='medecin__departement__nom',
        lookup_expr='icontains'
    )    
    default_ordering = ['-date_prescription']    
    class Meta:
        model = Prescription
        fields=['medecin', 'date_du', 'date_au', 'date', 'departement']