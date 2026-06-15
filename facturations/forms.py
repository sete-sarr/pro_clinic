from .models import Facture, DetailFacture
from django.forms.models import inlineformset_factory


ModelFormset = inlineformset_factory(
    Facture, DetailFacture,
    fields=["medicament", "prix", "quantite"],
      can_delete=True, extra =3
      )