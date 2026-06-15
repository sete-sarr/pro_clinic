import django_filters

import django_filters
from .models import Consultation

class ConsultationFilter(django_filters.FilterSet):
    patient = django_filters.CharFilter(
        field_name='patient__prenom',
        lookup_expr='icontains',
        label='Patient'
    )

    date_du = django_filters.DateFilter(
        field_name='date',
        lookup_expr='gte',
        label='Date début'
    )

    date_au = django_filters.DateFilter(
        field_name='date',
        lookup_expr='lte',
        label='Date fin'
    )

    class Meta:
        model = Consultation
        fields = ['patient', 'date_du', 'date_au']