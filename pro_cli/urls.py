"""
URL configuration for pro_cli project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    
    
    path('admin/', admin.site.urls),
    path('',  include( 'comptes.urls', namespace='comptes')),
    path('consultations/', include('consultations.urls', namespace='consultations')),
    path('rendez/vous/', include('rendez_vous.urls', namespace='rendez_vous')),
    path('patient/', include('patient.urls', namespace='patient')),
    path('facturations/', include('facturations.urls', namespace='facturations')),
    path('prescriptions/', include('prescriptions.urls', namespace='prescriptions')),

    # urls for the APIs
    path('api/', include('comptes.api.urls')),
    path('api/', include('facturations.api.urls')),
    path('api/', include('prescriptions.api.urls')),
    path('api/', include('consultations.api.urls')),
    path('api/', include('rendez_vous.api.urls')),

     
   
]
