from django.contrib import admin
from .models import Item, Movimentacao # Importa nossos modelos

# --- Configuração do Painel Admin ---

class ItemAdmin(admin.ModelAdmin):
    # list_display deve conter o método 'precisa_repor'
    list_display = ('nome', 'quantidade', 'localizacao', 'estoque_minimo', 'precisa_repor', 'created_at')
    
    # list_filter usa o método 'precisa_repor' como filtro
    list_filter = ('localizacao', 'precisa_repor') 
    
    # Campos onde se pode pesquisar
    search_fields = ('nome', 'descricao')
    # Campos apenas leitura
    readonly_fields = ('created_at', 'updated_at')

# Torna a listagem de Movimentacoes mais útil
class MovimentacaoAdmin(admin.ModelAdmin):
    # Campos exibidos na tela de listagem
    list_display = ('item', 'tipo', 'quantidade_movimentada', 'responsavel', 'data_movimentacao')
    # Campos que podem ser filtrados
    list_filter = ('tipo', 'data_movimentacao')
    # Campos onde se pode pesquisar
    search_fields = ('item__nome', 'responsavel')
    # Torna a data de movimentação apenas leitura
    readonly_fields = ('data_movimentacao',)

# --- Registro dos Modelos ---

admin.site.register(Item, ItemAdmin)
admin.site.register(Movimentacao, MovimentacaoAdmin)
