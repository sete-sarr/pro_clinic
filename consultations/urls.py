from . import views
from django.urls import path
app_name='consultations'

urlpatterns =[
    path('list/',
         views.ConsultationListView.as_view(),
           name='list'),
    path('detail/<int:pk>/', 
         views.ConsultationDetailView.as_view(), 
         name='detail'),
    path('modifier/<int:pk>/', 
         views.ConsultationActualiserView.as_view(),
         name='modifier'),

     path('creer/',
         views.ConsultationCreateView.as_view(),
           name='creer'),
     path('supprimer/<int:pk>/',     
         views.ConsultationSupprimerView.as_view(),
         name='supprimer'),    
]

