from django.db import models

# get_user_model() returns the User model that is active in this project
from django.contrib.auth import get_user_model

from compte.models import NkamotoBase
from django.utils import timezone
User = get_user_model()


class TypePlan(NkamotoBase):
    """
    Name : TypePlan
    Description : Modèle pour le type de plan
    author : DonaldProgrammeur
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text='Durée en jours')
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        
        if self.is_default:
            # Ensures that only one plan is default
            TypePlan.objects.filter(is_default=True).update(is_default=False)
            
        super().save(*args, **kwargs)
        

class Payment(NkamotoBase):
    
    # Payment status
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    
    STATUS_CHOICES = (
        (PENDING, 'En attente'),
        (COMPLETED, 'Complété'),
        (FAILED, 'Échoué'),
    )
    
    # Payment type
    DEPOT = 'DEPOT'
    RETRAIT = 'RETRAIT'
    TYPE_CHOICES = (
        (DEPOT, 'Dépôt'),
        (RETRAIT, 'Retrait'),
    )
    
    # Payment method
    MOBILE_MONEY = 'MOBILE_MONEY'
    CASH = 'CASH'
    METHOD_CHOICES = (
        (MOBILE_MONEY, 'Mobile Money'),
        (CASH, 'Cash'),
    )
    
    # Payment details
    order_number = models.CharField(max_length=255, unique=True, blank=True)
    type_plan = models.ForeignKey(TypePlan, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=DEPOT)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES, default=MOBILE_MONEY)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    comment = models.TextField(null=True, blank=True)
    fraud = models.BooleanField(default=False)
    active_from = models.DateTimeField(null=True, blank=True)
    active_to = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return self.order_number
    
    
    def payment_still_active(self):
        if self.active_to:
            _q = self.active_to > timezone.now()
            if _q:
                self.is_active = True
                self.save()
                return True
        self.is_active = False 
        self.save()   
        return False

