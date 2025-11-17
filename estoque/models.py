from django.db import models

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
        
    def precisa_repor(self):
        """
        HS-12: Verifica se a quantidade atual está abaixo ou igual ao estoque mínimo.
        """
        return self.quantidade <= self.estoque_minimo
