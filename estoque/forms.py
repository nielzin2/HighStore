from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    """
    Formulário para criar e editar um Item, incluindo o Estoque Mínimo (HS-11).
    """
    class Meta:
        model = Item
        # HS-11: Novo campo 'estoque_minimo' incluído
        fields = ['nome', 'descricao', 'quantidade', 'localizacao', 'estoque_minimo'] 
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }
