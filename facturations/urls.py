from django.urls import path
from . import views
app_name='facturations'
urlpatterns=[
    path('list/', views.ListFactureView.as_view(), name="list_factures"),
    path('creer/',views.CreerFactureView.as_view(), name="creer_facture"),
    path('modifier/<int:pk>/', views.ActualiserFactureView.as_view(), name="actualiser_facture"),
    path('supprimer/<int:pk>/', views.SupprimerFactureView.as_view(), name="supprimer_facture"),
    path('creer/detail/<int:pk>/', views.CreerDetailFactureCustomView.as_view(), name='creer_detail'),
    path('facture/pdf/<int:pk>/', views.facture_pdf, name='facture_pdf'),


]