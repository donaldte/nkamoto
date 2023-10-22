from django.shortcuts import render

# Importez les modules nécessaires
import uuid
from django.shortcuts import render
from django.http import JsonResponse
from .models import Payment
from django.conf import settings
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Votre vue Django
def generate_payment():

    # Générez un numéro de paiement unique
    unique_id = uuid.uuid4().hex[:7]  # Les 7 premiers caractères hexadécimaux de l'UUID généré

    number = Payment.objects.all().count() + 1
    # Structure du numéro de paiement
    order_number = f"NK-{number}-{unique_id}"
    
    return order_number



class PaymentView(LoginRequiredMixin, View):
    
    template_name = 'payment.html'
    """ let order_number = "{{order_number}}";
        let agency_code = "{{agency_code}}";
        let secure_code = "{{secure_code}}";
        let domain_name = "{{domain_name}}";
        let url_redirection_success = "{{url_redirection_success}}";
        let url_redirection_failed = "{{url_redirection_failed}}";
        let amount = "{{ amount}}";
        let city = "{{city}}";
        let email = "{{email}}";
        let clientFirstName = "John";
        let clientLastName = "Doe";
        let clientPhone = "{{clientPhone}}";"""
    
    def get(self, request, *args, **kwargs):
        
        
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    

    
    
    
    
    


