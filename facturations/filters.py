import django_filters
from .models import Facture

class FactureFilter(django_filters.FilterSet):
    date_du = django_filters.DateFilter(field_name="date", label="Date_du", lookup_expr="gte")

    date_au = django_filters.DateFilter(field_name="date", label="Date_au", lookup_expr="lte")
    patient = django_filters.CharFilter(field_name="patient__prenom",label="patient", lookup_expr="icontains")
    class Meta:
        model = Facture
        fields=["date_du", "date_au","patient"]
