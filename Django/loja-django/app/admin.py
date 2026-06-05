from django.contrib import admin
from app.models import Categoria, Produto, Compra


admin.site.register(Categoria)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'preco', 'categoria', 'imagem')
    search_fields = ('nome',)
    list_filter = ('categoria', 'preco')


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'produto_nome', 'valor', 'quantidade', 'data', 'avaliado')
    list_filter = ('avaliado', 'data')
    search_fields = ('usuario__username', 'produto_nome')
    date_hierarchy = 'data'