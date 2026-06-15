from rest_framework import serializers
from prescriptions.models import Prescription, ItemsPrescription
from medecin.models import Medecin
from consultations.models import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'
class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields =['nom','prenom','specialite']

class ItemsPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsPrescription
        fields =['id','medicament','dosage','frequence','duree', 'quantite','instructions']


class PrescriptionSerializer(serializers.ModelSerializer):
    medecin = MedecinSerializer(read_only=True)
    consultation = ConsultationSerializer(read_only=True)
    details_prescription = ItemsPrescriptionSerializer(
                                 many=True,
                                 read_only=True,
                                 source='lignes'
                                 )
    
    class Meta:
        model = Prescription
        fields =['id','date_prescription','medecin','consultation','details_prescription']



       