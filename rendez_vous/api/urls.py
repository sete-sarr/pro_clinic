from django.urls import path
from .views import RendezVousListView, RendezVousDetailView

urlpatterns=[
    path('rendez-vous/', RendezVousListView.as_view()),
    path('rendez-vous/<int:pk>/', RendezVousDetailView.as_view()),
]
