from django.shortcuts import get_object_or_404, render
from django.views import View
from commisariat.models import MotoVolee
from moto.models import ImageMoto, Moto


class IndexView(View):
    """
    Name: IndexView
    Description: This class is used to render the index page.
    Author: DonaldProgrammeur 
    """
    def get(self, request):
        return render(request, 'index.html')
    
    
# views.py
from django.shortcuts import render, redirect
from .forms import MotoForm
from django.contrib.auth.decorators import login_required

@login_required
def create_moto_with_images(request):
    """ 
    Name: create_moto_with_images
    Descripton: This function is used to create a moto with images.
    """
    if request.method == 'POST':
        moto_form = MotoForm(request.POST)

        if moto_form.is_valid():
            moto = moto_form.save(commit=False)
            moto.proprietaire = request.user
            moto.save()
            for image in request.FILES.getlist('image'):
                ImageMoto.objects.create(moto=moto, image=image)

            return redirect('moto:detail_moto', pk=moto.pk)  # Redirigez vers une page de succès
    
    return render(request, 'moto/create_moto.html')
    

def detail_about_moto(request, *args, **kwargs):
    """
    Name: detail_about_moto
    Description: This function is used to display the details of a moto.
    """
    pk = kwargs.get('pk')
    motos = Moto.objects.filter(pk=pk, proprietaire=request.user)
    moto = None
    if motos.exists():
        moto = motos.first()
    return render(request, 'moto/detail_moto.html', {'moto': moto})

@login_required
def list_moto(request):
    """
    Name: list_moto
    Description: This function is used to display the list of motos.
    """
    motos = Moto.objects.filter(proprietaire=request.user)
    return render(request, 'moto/list_moto.html', {'motos': motos})

@login_required
def list_moto_volee(request):
    """
    Name: list_moto_volee
    Description: This function is used to display the list steal moto.
    """
    motos = MotoVolee.objects.all()
    return render(request, 'moto/liste_moto_volee.html', {'motos': motos})