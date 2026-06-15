from django.urls import path
from . import views
app_name='prescriptions'
urlpatterns=[
    path('Prescriptions/', views.PrescriptionListView.as_view(), name='list_prescriptions'),
    path('Prescriptions/<int:pk>/', views.PrescriptionDetailView.as_view(), name='prescription_detail'),
    path('Prescriptions/create/', views.CreatePrescriptionView.as_view(), name='create_prescription'),
    path('Prescriptions/<int:pk>/update/', views.UpdatePrescriptionView.as_view(), name='update_prescription'),
    path('Prescriptions/<int:pk>/delete/', views.DeletePrescriptionView.as_view(), name='delete_prescription'),
    path('prescriptions/create/detail/<int:pk>/', views.CreateDetailPrescriptionView.as_view(), name='create_detail_prescription'),
    path('prescriptions/<int:pk>/pdf/', views.prescription_pdf, name='prescription_pdf')
]   