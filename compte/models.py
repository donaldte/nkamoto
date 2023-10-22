import datetime
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
    on_trial = models.BooleanField(default=True)
    
    
    # on trial is just for testing purposes of 13 days from the day of registration
    
    
    def still_on_trial(self):
        registration_date = self.created_at.date()
        today = datetime.date.today()
        difference = today - registration_date
        if difference.days > 13:
            self.on_trial = False
            self.save()
        return difference.days <= 13
    
    
    


class Profile(NkamotoBase):
    """
    Name : Profile
    Description : Modèle pour le profil des utilisateurs
    author : DonaldProgrammeur
    """
    numero_telephone = models.CharField(max_length=15)
    adresse_residence = models.CharField(max_length=255)
    numero_carte_identite = models.CharField(max_length=255)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo_profil = models.ImageField(upload_to='profile/', null=True, blank=True)
