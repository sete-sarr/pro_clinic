from django.urls import path
from .views import ConsultationListView

urlpatterns=[
    path('consultations/', ConsultationListView.as_view()),
]
