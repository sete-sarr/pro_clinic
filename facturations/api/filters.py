import django_filters 
from facturations.models import Facture
class FactureFilterSet(django_filters.FilterSet):

    medecin = django_filters.CharFilter(
        field_name='medecin__prenom',
        lookup_expr='icontains'
        )
    date_du = django_filters.DateFilter(
        field_name='date',
          lookup_expr='gte'
          )
    date_au = django_filters.DateFilter(
        field_name='date',
        lookup_expr='lte'
        )
    date = django_filters.DateFilter(
        field_name='date',
        lookup_expr='iexact'
        )
    class Meta:
        model = Facture
        fields=['medecin', 'date_du', 'date_au', 'date']