import django_filters
from .models import Prescription
class PrescriptionFilter(django_filters.FilterSet):
    date_du = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_au = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    patient = django_filters.CharFilter(field_name='patient__nom', lookup_expr='icontains', label='Nom du patient')
    medecin = django_filters.CharFilter(field_name='medecin__nom', lookup_expr='icontains', label='Nom du médecin')
    class Meta:
        model = Prescription
        fields = ['date_du', 'date_au', 'patient', 'medecin']