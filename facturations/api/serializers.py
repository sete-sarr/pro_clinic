from rest_framework import serializers
from facturations.models import Facture, DetailFacture

from medecin.models import Medecin
class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields =['nom','prenom','specialite']

class DetailFactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailFacture
        fields =['id','medicament','prix','quantite']


class FactureSerializer(serializers.ModelSerializer):
    medecin = MedecinSerializer(read_only=True)
    details_facture = DetailFactureSerializer(
                             many=True,
                             read_only=True
                            
                             )
    prix_total = serializers.DecimalField(
    max_digits=12,
    decimal_places=2,
    read_only=True
)
    class Meta:
        model = Facture
        fields =['id','date','payee','medecin','details_facture','prix_total']

    