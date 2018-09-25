from django.forms import ModelForm
from .models import Segurado


class DadosPessoaisForm(ModelForm):
    class Meta:
        model = Segurado
        fields = '__all__'
