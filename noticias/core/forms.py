from django import forms
from .models import Contacto , Noticia
from django.contrib.auth.forms import UserCreationForm
class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets={
            "Fecha":forms.SelectDateWidget()
            }