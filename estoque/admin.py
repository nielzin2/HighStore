from django.contrib import admin
from .models import Item, Movimentacao

# --- Configuração do Painel Admin ---

class ItemAdmin(admin.ModelAdmin):
    # list_display usa o método 'estoque_baixo' para mostrar o status (OK)
    list_display = ('nome', 'quantidade', 'localizacao', 'estoque_minimo', 'estoque_baixo', 'created_at')
    
    # CORREÇÃO DEFINITIVA: Mudamos o filtro para um campo REAL do BD ('estoque_minimo')
    # Assim, o Django não executa a checagem complexa que está falhando no seu ambiente.
    list_filter = ('localizacao', 'estoque_minimo') 
    
    search_fields = ('nome', 'descricao')
    readonly_fields = ('created_at', 'updated_at')

class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('item', 'tipo', 'quantidade_movimentada', 'responsavel', 'data_movimentacao')
    list_filter = ('tipo', 'data_movimentacao')
    search_fields = ('item__nome', 'responsavel')
    readonly_fields = ('data_movimentacao',)

# --- Registro dos Modelos ---

admin.site.register(Item, ItemAdmin)
admin.site.register(Movimentacao, MovimentacaoAdmin)
