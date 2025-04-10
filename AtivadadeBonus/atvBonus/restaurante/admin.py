from django.contrib import admin

from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome_categoria",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome_produto", "preco", "descricao", "categoria")

    list_filter = ("nome_produto", "categoria")