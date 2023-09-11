from django.db import models

from compte.models import CustomUser, NkamotoBase

class DeclarationVol(NkamotoBase):
    """
    Modèle pour enregistrer les déclarations de vol, héritant de NkamotoBase.
    """
    utilisateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    moto = models.ForeignKey('moto.Moto', on_delete=models.CASCADE)
    date_vol = models.DateField()
    quartier = models.CharField(max_length=255)
    commentaire = models.TextField()

class Moto(NkamotoBase):
    """
    Modèle pour enregistrer les informations sur les motos, héritant de NkamotoBase.
    """
    numero_matricule = models.CharField(max_length=255)
    type_moto = models.CharField(max_length=255)
    proprietaire = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.numero_matricule

class ImageMoto(NkamotoBase):
    """
    Modèle pour stocker les images des motos, héritant de NkamotoBase.
    """
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='motos/')
    
    def __str__(self):
        return f"Image de {self.moto}"