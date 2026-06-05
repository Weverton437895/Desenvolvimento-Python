from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} — {self.assunto}"


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome


class Compra(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='compras'
    )
    produto_nome = models.CharField(max_length=200)
    produto_db = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=1)
    data = models.DateTimeField(auto_now_add=True)
    avaliado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return f"{self.usuario.username} — {self.produto_nome}"