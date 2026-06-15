from rest_framework import  serializers
from rendez_vous.models import RendezVous
from medecin.models import Medecin
from departement.models import Departement

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ['nom','description']

class MedecinSerializer(serializers.ModelSerializer):
    departement = DepartementSerializer(read_only=True)
    class Meta:
        model = Medecin
        fields = ['prenom', 'nom', 'specialite', 'departement']
class RendezVousSerializer(serializers.ModelSerializer):
    medecin = MedecinSerializer(read_only=True)
    class Meta:
        model =  RendezVous
        fields=['id',   'date','heure' , 'statut', 'created_at', 'medecin']
