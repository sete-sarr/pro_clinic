from django.urls import path
from .views import ConsultationListView, ConsultationDetailView

urlpatterns=[
    path('consultations/', ConsultationListView.as_view()),
    path('consultations/<int:pk>/', ConsultationDetailView.as_view()),
]
