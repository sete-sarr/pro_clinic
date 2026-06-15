from django.urls import path
from .views import SendOptAPIView, VerifyOtpAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('envoyer/otp/', SendOptAPIView.as_view(), name='send-otp'),   
    path('verify-otp/', VerifyOtpAPIView.as_view(), name='verify-otp'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh",
),
]