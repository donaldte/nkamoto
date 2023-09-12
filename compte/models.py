from django.db import models
from django.contrib.auth.models import AbstractUser

class NkamotoBase(models.Model):
    """
    Classe de base pour tous les modèles de l'application NKAMOTO,
    contenant des champs tels que la date de création et la date de modification.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser, NkamotoBase):
    """
    Modèle personnalisé pour les utilisateurs, héritant de NkamotoBase.
    """
    is_commissariat = models.BooleanField(default=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    
class Profile(NkamotoBase):
    """
    Name: Profile
    Description: Modèle pour le profil des utilisateurs
    author: DonaldProgrammeur
    """
    numero_telephone = models.CharField(max_length=15)
    adresse_residence = models.CharField(max_length=255) 
    numero_carte_identite = models.CharField(max_length=255)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo_profil = models.ImageField(upload_to='profile/', null=True, blank=True)
       