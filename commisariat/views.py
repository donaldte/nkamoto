from django.shortcuts import render
from .models import  MotoVolee
# Create your views here.


def detail_moto_volee(request, *args, **kwargs):
    """
    Name: detail_moto_volee
    Description: This function is used to display the details of a moto.
    """
    pk = kwargs.get('pk')
    motos = MotoVolee.objects.filter(pk=pk)
    moto = None
    if motos.exists():
        moto = motos.first()
    return render(request, 'commisariat/detail_moto_volee.html', {'moto': moto})