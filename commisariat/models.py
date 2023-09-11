from django.db import models

from compte.models import CustomUser, NkamotoBase
from moto.models import Moto

class Commissariat(NkamotoBase):
    """
    Modèle pour enregistrer les informations sur les commissariats, héritant de NkamotoBase.
    """
    nom_commissariat = models.CharField(max_length=255)
    adresse_commissariat = models.CharField(max_length=255)
    responsable = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_commissariat

class MotoVolee(NkamotoBase):
    """
    Modèle pour enregistrer les motos trouvées dans les commissariats, héritant de NkamotoBase.
    """
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    commissariat = models.ForeignKey(Commissariat, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.moto} trouvée au commissariat {self.commissariat}"
