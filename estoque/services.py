# estoque/services.py

from .models import Item

# Função 1: Lógica para Listas e Dicionários (Item 2 da Ficha)
def obter_alertas_estoque_baixo():
    """
    Retorna uma lista de dicionários contendo itens com estoque baixo.
    Isso cumpre o requisito de manipulação explícita de listas e dicionários.
    """
    
    # 1. Recupera todos os itens que estão com estoque baixo (lógica)
    itens_em_alerta = Item.objects.filter(quantidade__lte=models.F('estoque_minimo'))
    
    # 2. Converte o QuerySet (objeto Django) em uma Lista de Dicionários (estrutura Python nativa)
    lista_alertas = []
    for item in itens_em_alerta:
        lista_alertas.append({
            'id': item.id,
            'nome': item.nome,
            'quantidade_atual': item.quantidade,
            'estoque_minimo': item.estoque_minimo,
            'necessidade': item.estoque_minimo - item.quantidade
        })
        
    return lista_alertas

# Função 2: Lógica de Movimentação (Exemplo de Função com Parâmetros e Retorno)
def processar_movimentacao(item_id, tipo, quantidade):
    """
    Processa a entrada ou saída de estoque de um item.
    Retorna True em caso de sucesso, False se houver erro (ex: estoque insuficiente).
    """
    try:
        item = Item.objects.get(pk=item_id)
        
        if tipo == 'entrada':
            item.quantidade += quantidade
        elif tipo == 'saida':
            if item.quantidade < quantidade:
                # Retorna False se a saída exceder o estoque atual
                return False 
            item.quantidade -= quantidade
        
        item.save()
        return True
        
    except Item.DoesNotExist:
        return False
        
    except Exception as e:
        # Lógica de erro mais robusta
        print(f"Erro ao processar movimentação: {e}")
        return False
