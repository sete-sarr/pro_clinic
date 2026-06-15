from consultations.models import Consultation
from .serializers import ConsultationSerializer
from rest_framework import generics
from rest_framework.filters import  OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ConsultationFilter



class BaseView(generics.GenericAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    filter_backends = [DjangoFilterBackend , OrderingFilter ]
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_class = ConsultationFilter
    ordering_fields = [
        'date',
    ]
    ordering = ['-date']

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.select_related(
            'medecin'
        ).filter(
            patient__utilisateur=self.request.user
        )


class ConsultationListView(BaseView, generics.ListAPIView):
    pass


class ConsultationDetailView(BaseView, generics.RetrieveAPIView):
    pass