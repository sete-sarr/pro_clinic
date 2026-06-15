from rest_framework import  serializers
from consultations.models import Consultation
from medecins.models import Medecin

class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = ['prenom', 'nom', 'specialite']
class ConsultationSerializer(serializers.ModelSerializer):
    medecin = MedecinSerializer(read_only=True)
    class Meta:
        model =  Consultation
        fields=['id', 'patient', 'medecin', 'date','diagnostic' , 'traitement']
