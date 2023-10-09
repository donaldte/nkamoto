from django.shortcuts import redirect, render
from django.views import View
# Create your views here.
from .models import CustomUser
from django.contrib import messages 

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from moto.models import Moto, DeclarationVol
from commisariat.models import MotoVolee



class DashboardView(LoginRequiredMixin, View):
    """
    Name: DashboardView
    Description: Vue pour le tableau de bord
    Author: DonaldProgrammeur
    """
    
    template_name = 'dashboard/index.html'
    
    def get(self, request):
        vos_motos = Moto.objects.filter(proprietaire=request.user).count()
        vos_moto_volee = DeclarationVol.objects.filter(utilisateur=request.user).count()
        tous_les_motos_volees = MotoVolee.objects.all().count()
        context = {
            'vos_motos': vos_motos,
            'vos_moto_volee': vos_moto_volee,
            'tous_les_motos_volees': tous_les_motos_volees
        }
        print(context)
        return render(request, self.template_name, context)
    
    
    def post(self, request):
        return render(request, self.template_name)

class CustomLoginView(View):
    """
    Name: LoginView
    Description: Vue pour la connexion des utilisateurs
    Author: DonaldProgrammeur 
    """
    template_name = 'compte/login.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenue, {user.username} Vous êtes connecté')
            return redirect('compte:dashboard')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
        return render(request, self.template_name)
    
    
    
class CustomUserCreateView(View):
    """
    Name: CustomUserCreateView
    Description: Vue pour la création des utilisateurs
    Author: DonaldProgrammeur
    """
    
    template_name = 'compte/register.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password_confirm')
        
        if password != confirm_password:
            messages.error(request, 'Les mots de passe ne correspondent pas')
            return render(request, self.template_name)
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur existe déjà. Veuillez en choisir un autre')
            return render(request, self.template_name)
        try:
            
            user = CustomUser.objects.create_user(username=username,
                                              email=email, password=password)
        except Exception as e:
            messages.error(request, f'Une erreur est survenue lors de la création de votre compte: {e}')
            return render(request, self.template_name)    
        
        if user is not None:
            messages.success(request, f'Votre compte a été créé avec succès')
            return redirect('compte:login')
        
        return render(request, self.template_name) 
    
    
class CustomUserUpdateView(View):
    """
    Name: CustomUserUpdateView
    Description: Vue pour la modification des utilisateurs
    Author: DonaldProgrammeur
    """
    
    template_name = 'compte/update_profile.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        pass    
    
    
def logout_view(request):
    """
    Name: logout_view
    Description: Vue pour la déconnexion des utilisateurs
    Author: DonaldProgrammeur
    """
    logout(request)
    messages.success(request, 'Vous êtes déconnecté')
    return redirect('compte:login') 


  

def error_404(request, exception):
    data = {}
    return render(request,'compte/404.html', data)  


def error_500(request):
    data = {}
    return render(request,'compte/500.html', data)