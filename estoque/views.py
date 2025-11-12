from django.shortcuts import render, redirect, get_object_or_404 # Importamos 'get_object_or_404'
from .models import Item
from .forms import ItemForm

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
    (Código da criação omitido aqui para brevidade, mas deve estar no seu arquivo)
    """
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque:lista_itens')
    else:
        form = ItemForm()

    context = {
        'form': form,
        'titulo': 'Adicionar Novo Item'
    }
    
    return render(request, 'estoque/novo_item.html', context)


# --- CRUD: UPDATE (U) ---

def editar_item(request, pk):
    """
    View responsável por carregar, exibir e processar o formulário de edição de item.
    """
    # 1. Busca o item pelo ID (pk), ou retorna 404 se não existir
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'POST':
        # 2. Quando o formulário é submetido, passa a requisição POST E a instância do item
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            # 3. Salva as alterações na instância existente
            form.save()
            return redirect('estoque:lista_itens')
    else:
        # 4. Se for GET, cria o formulário pré-preenchido com a instância
        form = ItemForm(instance=item)

    context = {
        'form': form,
        'titulo': f'Editar Item: {item.nome}'
    }
    
    # Reutiliza o template do novo item, pois o formulário é o mesmo!
    return render(request, 'estoque/novo_item.html', context)
