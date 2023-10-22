
from functools import wraps

from django.shortcuts import redirect
from django.contrib import messages
# implmentation of permission to access 
# functionnalities you can access if you are logged in and if you are on trial or you  have a active plan

# decorator for function check


def check_if_is_authenticated_and_on_trial_or_has_active_plan(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        user = request.user
        payments = user.payments.filter(is_active=True)
        if payments:
            payments = payments.first()
        if user.is_authenticated:
            if user.stil_on_trial():
                return function(request, *args, **kwargs)
            
            elif payments and payments.payment_still_active():
                return function(request, *args, **kwargs)
            else:
                messages.info(request, 'Vous devez avoir un plan actif pour accéder à cette page car votre dernière plan a expiré')
                return redirect('payment:payment')
        else:
            messages.info(request, 'Vous devez être connecté pour accéder à cette page')
            return redirect('compte:login')
    return wrap

# form mixin now

class CheckIfIsAuthenticatedAndOnTrialOrHasActivePlanMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        payments = user.payments.filter(is_active=True)
        if payments:
            payments = payments.first()
        if user.is_authenticated:
            if user.stil_on_trial():
                return super().dispatch(request, *args, **kwargs)
            
            elif payments and payments.payment_still_active():
                return super().dispatch(request, *args, **kwargs)
            else:
                messages.info(request, 'Vous devez avoir un plan actif pour accéder à cette page car votre dernière plan a expiré')
                return redirect('payment:payment')
        else:
            messages.info(request, 'Vous devez être connecté pour accéder à cette page')
            return redirect('compte:login')