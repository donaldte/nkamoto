from django.db import models

from compte.models import CustomUser, NkamotoBase
from moto.models import Moto
from django.urls import reverse
class Commissariat(NkamotoBase):
    """
    Modèle pour enregistrer les informations sur les commissariats, héritant de NkamotoBase.
    """
    nom_commissariat = models.CharField(max_length=255)
    adresse_commissariat = models.CharField(max_length=255)
    responsable_commissariat = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    telephone_commissariat = models.CharField(max_length=15, null=True, blank=True)
    email_commissariat = models.EmailField(null=True, blank=True)
    ville_commissariat = models.CharField(max_length=255, null=True, blank=True)
    

    def __str__(self):
        return self.nom_commissariat

class MotoVolee(NkamotoBase):
    """
    Modèle pour enregistrer les motos trouvées dans les commissariats, héritant de NkamotoBase.
    """
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    commissariat = models.ForeignKey(Commissariat, on_delete=models.CASCADE, null=True, blank=True)
    commentaire = models.TextField(null=True, blank=True)
    date_vol = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.moto} trouvée au commissariat {self.commissariat}"
    
    def get_absolute_url(self):
        return reverse("commisariat:detail_moto_volee", kwargs={"pk": self.pk})
