from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.db.models import Q, F

# --- CRUD: READ (R) com Busca/Filtro (HS-10) ---

def lista_itens(request):
    """
    Lista todos os itens no estoque, com suporte à busca por nome (HS-10).
    """
    itens = Item.objects.all().order_by('nome')
    query = request.GET.get('q')
    
    if query:
        itens = itens.filter(
            Q(nome__icontains=query)
        ).distinct()
    
    context = {
        'itens': itens,
        'titulo': 'Estoque Geral',
    }
    return render(request, 'estoque/lista_itens.html', context)

# --- GESTÃO: ALERTA DE ESTOQUE MÍNIMO (HS-12) ---

def alerta_estoque(request):
    """
    Lista todos os itens cuja quantidade atual está abaixo ou igual ao estoque_minimo.
    """
    # Filtra os itens onde 'quantidade' é menor ou igual a 'estoque_minimo' usando F (Field)
    itens_criticos = Item.objects.filter(
        quantidade__lte=F('estoque_minimo')
    ).order_by('quantidade') 
    
    context = {
        'itens': itens_criticos,
        'titulo': 'ALERTA: Itens Abaixo do Estoque Mínimo',
        'is_alerta_view': True # Flag para ajustes no template
    }
    
    # Reutiliza o template de listagem
    return render(request, 'estoque/lista_itens.html', context)

# --- CRUD: CREATE (C) ---

def adicionar_item(request):
    """
    Adiciona um novo item ao estoque.
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
        'titulo': 'Adicionar Novo Item',
    }
    return render(request, 'estoque/item_form.html', context)

# --- CRUD: READ (R) - Detalhe ---

# Esta view não foi criada, mas é essencial para o link de nome na listagem
def detalhe_item(request, pk):
    """
    Exibe os detalhes de um item específico.
    """
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item,
        'titulo': f'Detalhe: {item.nome}',
    }
    return render(request, 'estoque/detalhe_item.html', context)


# --- CRUD: UPDATE (U) ---

def editar_item(request, pk):
    """
    Edita um item existente.
    """
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('estoque:lista_itens')
    else:
        form = ItemForm(instance=item)
    
    context = {
        'form': form,
        'titulo': f'Editar Item: {item.nome}',
    }
    return render(request, 'estoque/item_form.html', context)

# --- CRUD: DELETE (D) ---

def deletar_item(request, pk):
    """
    Deleta um item do estoque.
    """
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('estoque:lista_itens')
        
    context = {
        'item': item,
        'titulo': f'Deletar Item: {item.nome}',
    }
    return render(request, 'estoque/delete_confirm.html', context)
