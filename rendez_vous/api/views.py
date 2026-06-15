from rendez_vous.models import RendezVous
from .serializers import RendezVousSerializer
from rest_framework import generics
from rest_framework.filters import  OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RendezVousFilterSet



class BaseView(generics.GenericAPIView):
    queryset = RendezVous.objects.all()
    serializer_class = RendezVousSerializer
    filter_backends = [DjangoFilterBackend , OrderingFilter ]
    
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_class = RendezVousFilterSet
    

    # def get_queryset(self):
    #     qs = super().get_queryset()

    #     return qs.select_related(
    #         'medecin'
    #     ).filter(
    #         patient__utilisateur=self.request.user
    #     )


class RendezVousListView(BaseView, generics.ListAPIView):
    pass


class RendezVousDetailView(BaseView, generics.RetrieveAPIView):
    pass