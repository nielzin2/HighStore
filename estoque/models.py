from django.db import models

# O nome desta classe será usado pelo Django para criar a tabela 'estoque_item' no DB.
class Item(models.Model):
    # O campo 'id' é criado automaticamente como Primary Key pelo Django.

    nome = models.CharField(
        max_length=200, 
        unique=True, 
        verbose_name="Nome do Item"
    )

    quantidade = models.IntegerField(
        default=0, 
        verbose_name="Quantidade em Estoque"
    )

    unidade_medida = models.CharField(
        max_length=50, 
        verbose_name="Unidade de Medida"
    )

    class Meta:
        # Nome da tabela no plural para facilitar a visualização no admin/código
        verbose_name_plural = "Itens"
        ordering = ['nome'] # Ordena por nome por padrão

    def __str__(self):
        # Representação do objeto Item em texto
        return f"{self.nome} ({self.quantidade} {self.unidade_medida})"
