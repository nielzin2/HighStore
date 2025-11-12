from django.shortcuts import render, redirect # Importamos 'redirect'
from .models import Item
from .forms import ItemForm # Importamos o formulário que acabamos de criar

# --- CRUD: READ (R) ---

def lista_itens(request):
    """
    View responsável por buscar todos os itens no banco de dados 
    e enviá-los para o template de listagem.
    """
    itens = Item.objects.all().order_by('nome')
    
    context = {
        'itens': itens,
        'titulo': 'Estoque Geral do Almoxarifado'
    }
    
    return render(request, 'estoque/lista_itens.html', context)


# --- CRUD: CREATE (C) ---

def adicionar_item(request):
    """
    View responsável por exibir e processar o formulário de adição de item.
    """
    if request.method == 'POST':
        # 1. Se o método for POST, os dados foram submetidos
        form = ItemForm(request.POST)
        if form.is_valid():
            # 2. Se a validação do formulário for bem-sucedida, salva no BD
            form.save()
            # 3. Redireciona o usuário para a lista após salvar
            return redirect('estoque:lista_itens')
    else:
        # Se o método for GET, exibe o formulário vazio
        form = ItemForm()

    context = {
        'form': form,
        'titulo': 'Adicionar Novo Item'
    }
    
    # Renderiza o template do formulário
    return render(request, 'estoque/novo_item.html', context)
