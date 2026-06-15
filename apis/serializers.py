from rest_framework import serializers
from gestions.models import *


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'




class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = '__all__'




class RendezVousSerializer(serializers.ModelSerializer):
   class Meta:
    model = RendezVous
    fields = '__all__'




class DossierMedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DossierMedical
        fields = '__all__'




class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'




class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'


class PaiementSerializer(serializers.ModelSerializer):

    class Meta:

        model = Paiement
        fields = '__all__'

