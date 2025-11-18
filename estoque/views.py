from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Movimentacao
from .forms import ItemForm, MovimentacaoForm
from django.db.models import Q, F
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required # NOVO: Importa o decorador de segurança
from .services import obter_alertas_estoque_baixo, processar_movimentacao

# --- VIEWS PROTEGIDAS COM @login_required (HS-15) ---

@login_required
def lista_itens(request):
    """
    Lista todos os itens no estoque, com suporte à busca por nome (HS-10).
    """
    # ... (código existente da lista_itens) ...
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

@login_required
def alerta_estoque(request):
    """
    Lista todos os itens cuja quantidade atual está abaixo ou igual ao estoque_minimo (HS-12).
    """
    # ... (código existente da alerta_estoque) ...
    itens_criticos = Item.objects.filter(
        quantidade__lte=F('estoque_minimo')
    ).order_by('quantidade') 
    
    context = {
        'itens': itens_criticos,
        'titulo': 'ALERTA: Itens Abaixo do Estoque Mínimo',
        'is_alerta_view': True
    }
    return render(request, 'estoque/lista_itens.html', context)

@login_required
def registrar_movimentacao(request, pk):
    """
    Processa o formulário de entrada ou saída de estoque e atualiza a quantidade do item (HS-14).
    """
    # ... (código existente da registrar_movimentacao) ...
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            quantidade_movimentada = form.cleaned_data['quantidade_movimentada']
            tipo = form.cleaned_data['tipo']
            
            with transaction.atomic():
                
                if tipo == 'S':
                    if item.quantidade < quantidade_movimentada:
                        messages.error(request, "ERRO: Quantidade insuficiente em estoque.")
                        return redirect('estoque:registrar_movimentacao', pk=pk)
                    
                    item.quantidade -= quantidade_movimentada
                    
                elif tipo == 'E':
                    item.quantidade += quantidade_movimentada
                
                movimentacao = form.save(commit=False)
                movimentacao.item = item
                movimentacao.save()
                
                item.save()
            
            messages.success(request, f"Movimentação registrada e estoque de {item.nome} atualizado.")
            return redirect('estoque:lista_itens')
            
    else:
        form = MovimentacaoForm()
        
    context = {
        'item': item,
        'form': form,
        'titulo': f'Movimentar Estoque: {item.nome}'
    }
    return render(request, 'estoque/movimentar_estoque.html', context)
    
@login_required
def historico_movimentacoes(request):
    """
    Lista todas as movimentações registradas no sistema (HS-14).
    """
    # ... (código existente da historico_movimentacoes) ...
    movimentacoes = Movimentacao.objects.select_related('item').all()
    
    context = {
        'movimentacoes': movimentacoes,
        'titulo': 'Histórico de Movimentações'
    }
    return render(request, 'estoque/historico_movimentacoes.html', context)


@login_required
def adicionar_item(request):
    """
    Adiciona um novo item ao estoque.
    """
    # ... (código existente da adicionar_item) ...
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

@login_required
def detalhe_item(request, pk):
    """
    Exibe os detalhes de um item específico.
    """
    # ... (código existente da detalhe_item) ...
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item,
        'titulo': f'Detalhe: {item.nome}',
    }
    return render(request, 'estoque/detalhe_item.html', context)


@login_required
def editar_item(request, pk):
    """
    Edita um item existente.
    """
    # ... (código existente da editar_item) ...
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

@login_required
def deletar_item(request, pk):
    """
    Deleta um item do estoque.
    """
    # ... (código existente da deletar_item) ...
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('estoque:lista_itens')
        
    context = {
        'item': item,
        'titulo': f'Deletar Item: {item.nome}',
    }
    return render(request, 'estoque/delete_confirm.html', context)
