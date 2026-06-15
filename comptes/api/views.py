
from random import randint

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from patient.models import Patient
from comptes.models import OTP

from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny





class SendOptAPIView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):

        telephone = request.data.get("telephone")
        numero_patient = request.data.get("numero_patient")

        try:
            patient = Patient.objects.get(
                numero_patient=numero_patient,
                telephone=telephone
            )

        except Patient.DoesNotExist:
            return Response(
                {
                    "error": "Patient non trouvé"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if patient.utilisateur:
            return Response(
                {
                    "error": "Ce patient possède déjà un compte."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        OTP.objects.filter(
            patient=patient,
            is_used=False
        ).delete()

        code = str(randint(100000, 999999))

        otp = OTP.objects.create(
            patient=patient,
            code=code
        )

        print(
            f"OTP envoyé à {telephone} : {code}"
        )

        return Response(
            {
                "message": "OTP envoyé avec succès",
                "otp_id": otp.id,

                # uniquement en développement
                "otp": code,
            }
        )





class VerifyOtpAPIView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []


    def post(self, request):

        otp_id = request.data.get("otp_id")

        otp_code = request.data.get("otp")

        password = request.data.get(
            "password"
        )

        password_confirm = request.data.get(
            "password_confirm"
        )

        if password != password_confirm:
            return Response(
                {
                    "error":
                    "Les mots de passe ne correspondent pas."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            otp = OTP.objects.select_related(
                "patient"
            ).get(id=otp_id)

        except OTP.DoesNotExist:
            return Response(
                {
                    "error": "OTP introuvable."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if otp.is_used:
            return Response(
                {
                    "error":
                    "Ce code OTP a déjà été utilisé."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not otp.is_valid:
            return Response(
                {
                    "error":
                    "Le code OTP a expiré."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if otp.code != str(otp_code):
            return Response(
                {
                    "error": "OTP invalide."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        patient = otp.patient

        if patient.utilisateur:
            return Response(
                {
                    "error":
                    "Un compte existe déjà."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=patient.numero_patient,
            password=password
        )

        patient.utilisateur = user
        patient.save()

        otp.is_used = True
        otp.save()

        refresh = RefreshToken.for_user(
            user
        )

        return Response(
            {
                "refresh": str(refresh),

                "access": str(
                    refresh.access_token
                ),

                "message":
                "Compte activé avec succès."
            }
        ) 


        #  "otp_id": 10,
        #  "otp": "303804",
        #  "password": "sete1234",
        #  "password_confirm": "sete1234"     