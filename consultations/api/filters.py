import django_filters
class ConsultaionFilterSet(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date',lookup_expr='date', label='date')
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='date__gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='date__lte')
    class Meta:
        fields=['date', 'date_from', 'date_to']
    