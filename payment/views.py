from django.shortcuts import render

# Importez les modules nécessaires
import uuid
from django.shortcuts import render
from django.http import JsonResponse
from .models import Payment, TypePlan
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
    
    template_name = 'payment/payment.html'
    

    def get_info(self):
        agency_code = settings.AGENCY_CODE
        secure_code =  settings.SECURE_CODE
        domain_name = self.request.get_host()
        print(domain_name)
        order_number = generate_payment()
        domain_name = f"https://{domain_name}/"
        print(domain_name)
        return agency_code, secure_code, domain_name, order_number
        
    def get(self, request, *args, **kwargs):
        
        get_info = self.get_info()
        agency_code = get_info[0]
        secure_code = get_info[1]
        domain_name = get_info[2]
        order_number = get_info[3]
        url_redirection_success = f"{domain_name}payment/success"
        url_redirection_failed = f"{domain_name}payment/failed"
        amount = 1000
        city = "Douala"
        email = request.user.email
        clientFirstName = request.user.first_name
        clientLastName = request.user.last_name

        payment = Payment.objects.create(
            order_number=order_number,
            user=request.user
        )
        list_plan = TypePlan.objects.all()
        
        context = {
            'order_number': order_number,
            'url_redirection_success': url_redirection_success,
            'url_redirection_failed': url_redirection_failed,
            'amount': amount,
            'city': city,
            'email': email,
            'clientFirstName': clientFirstName,
            'clientLastName': clientLastName,
            'clientPhone': '',
            'agency_code': agency_code,
            'secure_code': secure_code,
            'list_plan': list_plan,
        }
      
        return render(request, self.template_name, context)
    
   
    

    
    
    
    
    


