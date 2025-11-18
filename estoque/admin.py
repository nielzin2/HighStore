from django.contrib import admin
from .models import Item, Movimentacao # Importa nossos modelos

# --- Configuração do Painel Admin ---

class ItemAdmin(admin.ModelAdmin):
    # list_display usa o novo método 'estoque_baixo'
    list_display = ('nome', 'quantidade', 'localizacao', 'estoque_minimo', 'estoque_baixo', 'created_at')
    
    # list_filter usa o novo método 'estoque_baixo'
    list_filter = ('localizacao', 'estoque_baixo') 
    
    search_fields = ('nome', 'descricao')
    readonly_fields = ('created_at', 'updated_at')

# Torna a listagem de Movimentacoes mais útil
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('item', 'tipo', 'quantidade_movimentada', 'responsavel', 'data_movimentacao')
    list_filter = ('tipo', 'data_movimentacao')
    search_fields = ('item__nome', 'responsavel')
    readonly_fields = ('data_movimentacao',)

# --- Registro dos Modelos ---

admin.site.register(Item, ItemAdmin)
admin.site.register(Movimentacao, MovimentacaoAdmin)
