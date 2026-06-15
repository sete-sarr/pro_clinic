import django_filters
from .models import RendezVous

class RendezVousFilter(django_filters.FilterSet):
    patient = django_filters.CharFilter(field_name='patient__prenom', lookup_expr='icontains', label='patient')
    date_du = django_filters.DateFilter(field_name='date', lookup_expr='year__gte', label='Date du')
    date_au = django_filters.DateFilter(field_name='date', lookup_expr='year__lte', label='Date AU')
    statut = django_filters.ChoiceFilter(
    field_name='statut',
    choices=RendezVous.STATUT_CHOICES,
    label='Statut'
)
    heure = django_filters.TimeFilter(field_name='heure', lookup_expr='iexact')
    class Meta:
        model = RendezVous
        fields=['patient', 'date_du', 'date_au',  'statut','heure']