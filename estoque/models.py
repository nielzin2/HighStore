from django.db import models
from django.contrib import admin 
from django.db.models import F 

# Tipos de Movimentação (usado para o campo 'tipo')
TIPO_MOVIMENTACAO = (
    ('E', 'Entrada (Adição)'),
    ('S', 'Saída (Retirada)'),
)

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    localizacao = models.CharField(max_length=50, blank=True, null=True)
    
    estoque_minimo = models.IntegerField(default=5, help_text="Quantidade mínima para alerta.")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
        
    @admin.display(boolean=True, description="Estoque Baixo")
    def estoque_baixo(self):
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
