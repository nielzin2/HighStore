from django.contrib import admin
from .models import Item, Movimentacao # Importa nossos modelos

# --- Configuração do Painel Admin (Opcional, mas profissional) ---

# Torna a listagem de Itens mais útil
class ItemAdmin(admin.ModelAdmin):
    # Campos exibidos na tela de listagem
    list_display = ('nome', 'quantidade', 'localizacao', 'estoque_minimo', 'precisa_repor')
    # Campos que podem ser filtrados
    list_filter = ('localizacao', 'precisa_repor')
    # Campos onde se pode pesquisar
    search_fields = ('nome', 'descricao')

# Torna a listagem de Movimentacoes mais útil
class MovimentacaoAdmin(admin.ModelAdmin):
    # Campos exibidos na tela de listagem
    list_display = ('item', 'tipo', 'quantidade_movimentada', 'responsavel', 'data_movimentacao')
    # Campos que podem ser filtrados
    list_filter = ('tipo', 'data_movimentacao')
    # Campos onde se pode pesquisar
    search_fields = ('item__nome', 'responsavel')
    # Torna a data de movimentação apenas leitura, pois é preenchida automaticamente
    readonly_fields = ('data_movimentacao',)

# --- Registro dos Modelos ---

admin.site.register(Item, ItemAdmin)
admin.site.register(Movimentacao, MovimentacaoAdmin)
