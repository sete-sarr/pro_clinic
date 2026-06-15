import django_filters
from rendez_vous.models import RendezVous
class RendezVousFilterSet(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date',lookup_expr='iexact', label='date')
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='date__gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='date__lte')
    Departement = django_filters.CharFilter(
        field_name='medecin__departement__nom',
        label='Département'
    )
    default_ordering = ['-date']
    class Meta:
        model = RendezVous
        fields=['date', 'date_from', 'date_to', 'Departement']
    