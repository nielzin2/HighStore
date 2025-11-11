from django.shortcuts import render
from .models import Item # Importa o nosso modelo de Item

# --- CRUD: READ (R) ---

def lista_itens(request):
    """
    View responsável por buscar todos os itens no banco de dados 
    e enviá-los para o template de listagem.
    """
    # Consulta ao banco de dados usando o ORM do Django
    # Equivalente a: SELECT * FROM Itens ORDER BY nome;
    itens = Item.objects.all().order_by('nome')
    
    # Contexto: Dicionário que passa os dados Python para o Template HTML
    context = {
        'itens': itens,
        'titulo': 'Estoque Geral do Almoxarifado'
    }
    
    # Renderiza o template 'lista_itens.html', passando os dados.
    return render(request, 'estoque/lista_itens.html', context)
