from django.forms import ModelForm
from .models import DadosPessoais

class DadosPessoaisForm(ModelForm):
    class Meta:
        model = DadosPessoais
        fields = '__all__'
