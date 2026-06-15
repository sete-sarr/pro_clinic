from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('rendezvous', RendezVousViewSet)
router.register('consultations', ConsultationViewSet)
router.register('factures', FactureViewSet)


urlpatterns = router.urls