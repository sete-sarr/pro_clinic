               
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .filters import FactureFilterSet
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import FactureSerializer
from facturations.models import Facture

class BaseMixinAPi(generics.GenericAPIView):
    permission_classes=[IsAuthenticated]
    filterSet_class = FactureFilterSet
    serializer_class = FactureSerializer
    # authentication_classes=[JWTAuthentication]
    queryset = Facture.objects.all()
    ordering_fields=['-date']
    filter_backends=[DjangoFilterBackend]
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return  qs.select_related('medecin').filter(patient__utilisateur=self.request.user)

class ListApi(BaseMixinAPi,generics.ListAPIView):
    pass
class DetailApi(BaseMixinAPi, generics.RetrieveAPIView):
    pass