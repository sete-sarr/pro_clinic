from django.urls import path
from . import views
urlpatterns=[
    path('facturations/', views.ListApi.as_view()),
    path('facturations/<int:pk>/', views.DetailApi.as_view()),
]