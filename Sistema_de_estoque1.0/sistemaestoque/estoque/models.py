from django.db import models


# Create your models here.

class ItemEstoque(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    descricao = models.TextField(blank=True, null=True)
    dataentrada = models.DateTimeField(auto_now_add=True)
    donoprenome = models.CharField(max_length=32, default='Sandeison')  
    donosobrenome = models.CharField(max_length=32, default='Fernandes') 
    localizacao = models.CharField(max_length=30, default='Armazém A')
    categoria = models.CharField(max_length=30, default='Geral')

    def __str__(self):
        return self.nome
    



class Item(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)

    @property
    def estoque_total(self):
        entradas = self.movimentacoes.filter(tipo='entrada').aggregate(total=models.Sum('quantidade'))['total'] or 0
        saidas = self.movimentacoes.filter(tipo='saida').aggregate(total=models.Sum('quantidade'))['total'] or 0
        return entradas - saidas

    def __str__(self):
        return self.nome


class Movimentacao(models.Model):
    TIPOS = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )

    item = models.ForeignKey(Item, related_name='movimentacoes', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.item.nome} ({self.quantidade})"

