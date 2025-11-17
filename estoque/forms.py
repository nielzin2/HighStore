from django import forms
from .models import Item, Movimentacao # Importa Movimentacao

class ItemForm(forms.ModelForm):
    """
    Formulário para criar e editar um Item.
    """
    class Meta:
        model = Item
        fields = ['nome', 'descricao', 'quantidade', 'localizacao', 'estoque_minimo'] 
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

# NOVO FORMULÁRIO (HS-14)
class MovimentacaoForm(forms.ModelForm):
    """
    Formulário para registrar entradas e saídas.
    """
    class Meta:
        model = Movimentacao
        # Excluímos 'item' e 'data_movimentacao' que serão preenchidos pela view
        fields = ['tipo', 'quantidade_movimentada', 'responsavel', 'observacao']
        labels = {
            'tipo': 'Tipo de Operação',
            'quantidade_movimentada': 'Quantidade',
            'responsavel': 'Responsável',
        }
