from django.urls import path
from .import views
app_name ='rendez_vous'

urlpatterns=[
    path('list/', views.RendezVousListView.as_view(), name='list'),

    path('detail/<int:pk>/', views.RendezVousDetailView.as_view(), name='detail'),

    path('modifier/<int:pk>/', views.RendezVousActualiserView.as_view(), name='modifier'),
    path('creer/', views.RendezVousCreateView.as_view(), name='creer'),
    path('supprimer/<int:pk>/', views.RendezVousDeleteView.as_view(), name='supprimer'),

    # urls.py
    path('search-patient/', views.search_patient, name='search_patient'),

    path('create-patient/', views.create_patient_ajax),

]
