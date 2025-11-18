from django.db import models
from django.contrib import admin # Importar admin
from django.db.models import F 

# Tipos de Movimentação (usado para o campo 'tipo')
TIPO_MOVIMENTACAO = (
    ('E', 'Entrada (Adição)'),
    ('S', 'Saída (Retirada)'),
)

class Item(models.Model):
    """
    Representa um item no estoque.
    """
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    localizacao = models.CharField(max_length=50, blank=True, null=True)
    
    # HS-11: Campo para Estoque Mínimo
    estoque_minimo = models.IntegerField(default=5, help_text="Quantidade mínima para alerta.")
    
    # HS-13: Campos de Data e Hora
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
        
    # CORREÇÃO HS-16: Método renomeado e com decorador para Admin
    @admin.display(boolean=True, description="Estoque Baixo")
    def estoque_baixo(self):
        """
        Verifica se a quantidade atual está abaixo ou igual ao estoque mínimo.
        """
        return self.quantidade <= self.estoque_minimo

# NOVO MODELO (HS-14)
class Movimentacao(models.Model):
    item = models.ForeignKey(
        Item, 
        on_delete=models.CASCADE, 
        related_name='movimentacoes',
        verbose_name="Item Movimentado"
    )
    tipo = models.CharField(max_length=1, choices=TIPO_MOVIMENTACAO)
    quantidade_movimentada = models.IntegerField()
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    responsavel = models.CharField(max_length=100, help_text="Nome do responsável pela operação.")
    observacao = models.TextField(blank=True, null=None)

    class Meta:
        ordering = ['-data_movimentacao']
        verbose_name_plural = "Movimentações"

    def __str__(self):
        operacao = "Entrada" if self.tipo == 'E' else "Saída"
        return f"{operacao} de {self.quantidade_movimentada}x {self.item.nome} por {self.responsavel}"
