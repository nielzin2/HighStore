from django import forms
from .models import Item

# Cria um formulário baseado no Modelo Item
class ItemForm(forms.ModelForm):
    # Meta class é usada para configurar o formulário, dizendo qual modelo usar
    class Meta:
        model = Item
        # Campos que queremos que apareçam no formulário
        fields = ['nome', 'quantidade', 'unidade_medida'] 
        
        # Opcional: Personalizar os rótulos dos campos no formulário
        labels = {
            'nome': 'Nome do Item',
            'quantidade': 'Quantidade Inicial',
            'unidade_medida': 'Unidade de Medida (ex: UN, M, CX)',
        }
