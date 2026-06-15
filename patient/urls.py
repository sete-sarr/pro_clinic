from django.urls import path
from .import views
app_name="patient"
urlpatterns=[
    path('list/patients', views.PatientListView.as_view(), name='list_patient'),
    path('creer/patients', views.PatientCreerView.as_view(), name='creation_patient'),
    path('actualiser/patients/<int:pk>', views.PatientActualiserView.as_view(), name='actualiser_patient'),
    path('detail/patient/<int:pk>', views.PatientDetailView.as_view(), name='detail_patient'),
    path('supprimer/patient/<int:pk>', views.PatientSupprimerView.as_view(), name='supprimer_patient'),
    
    


]