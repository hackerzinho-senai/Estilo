from django import forms # type: ignore
from .models import Musicas

class Musicasform(forms.ModelForm):
    class Meta:
        model = Musicas
        fields = ['nome', 'estilo']