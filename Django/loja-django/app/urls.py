from django.urls import path
from . import views

urlpatterns = [
    # ─── Home ───
    path('', views.index, name='index'),

    # ─── Páginas Públicas ───
    path('quem-somos/', views.quemSomos, name='quemsomos'),
    path('loja/', views.loja, name='loja'),
    path('contato/', views.addContato, name='addcontato'),

    # ─── Autenticação ───
    path('cadastro/', views.cadastrarUsuario, name='cadastro'),
    path('login/', views.loginUsuario, name='login'),
    path('logout/', views.logoutUsuario, name='logout'),

    # ─── Perfil do Cliente ───
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editarUsuario, name='editarusuario'),

    # ─── Compras ───
    path('comprarProduto/', views.comprarProdutoApi, name='comprarProdutoApi'),
    path('avaliar/<int:id_compra>/', views.avaliarCompra, name='avaliarCompra'),

    # ─── Dashboard ───
    path('dashboard/', views.dashboard, name='dashboard'),

    # ─── Usuários (Admin) ───
    path('dashboard/usuarios/', views.listarUsuarios, name='usuarios'),
    path('dashboard/usuarios/add/', views.addUsuarioAdmin, name='addusuarioadmin'),
    path('dashboard/usuarios/edit/<int:id_user>/', views.editUsuarioAdmin, name='editusuarioadmin'),
    path('dashboard/usuarios/del/<int:id_user>/', views.delUsuario, name='delusuario'),
    path('dashboard/avaliacoes/edit/<str:id_avaliacao>/',views.editarAvaliacaoAdmin,name='editaravaliacao'
),

    # ─── Categorias (Admin) ───
    path('dashboard/categorias/', views.listarCategoria, name='categoria'),
    path('dashboard/categorias/add/', views.addCategoria, name='addcategoria'),
    path('dashboard/categorias/edit/<int:id_cat>/', views.editCategoria, name='editcategoria'),
    path('dashboard/categorias/del/<int:id_cat>/', views.delCategoria, name='delcategoria'),

    # ─── Produtos (Admin) ───
    path('dashboard/produto/', views.produto, name='produto'),
    path('dashboard/produtos/add/', views.addProduto, name='addproduto'),
    path('dashboard/produtos/edit/<int:id_prod>/', views.editProduto, name='editproduto'),
    path('dashboard/produtos/del/<int:id_prod>/', views.delProduto, name='delProduto'),

    # ─── Contatos (Admin) ───
    path('dashboard/contatos/', views.listarContatoAdmin, name='contato'),
    path('dashboard/contatos/del/<int:id_contato>/', views.delContato, name='delcontato'),

    # ─── Compras (Admin) ───
    path('dashboard/compras/', views.listarComprasAdmin, name='comprasadmin'),
    path('dashboard/compras/del/<int:id_compra>/', views.delCompraAdmin, name='delcompraadmin'),

    # ─── Avaliações (Admin) ───
    path('dashboard/avaliacoes/', views.listarAvaliacoesAdmin, name='avaliacoesadmin'),
    path('dashboard/avaliacoes/del/<str:id_avaliacao>/', views.delAvaliacaoAdmin, name='delavaliacao'),
]