# forms.py
from django import forms
from .models import Moto, ImageMoto

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['numero_matricule', 'type_moto']
        

class ImageMotoForm(forms.ModelForm):
    class Meta:
        model = ImageMoto
        fields = ['image']

