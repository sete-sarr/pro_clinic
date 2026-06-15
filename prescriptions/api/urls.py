from django.urls import path
from . import views
urlpatterns=[
    path('prescriptions/', views.ListApi.as_view()),
    path('prescriptions/<int:pk>/', views.DetailApi.as_view()),
]