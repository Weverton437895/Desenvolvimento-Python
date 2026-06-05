from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Group, User
from django.contrib import messages
import requests

from app.models import Categoria, Contato, Produto, Compra
from app.forms import FormCategoria, FormContato, ProdutoForm, FormUsuario, FormEditarUsuario
from firebase_config import db


# ─────────────────────────────────────
# Páginas Públicas
# ─────────────────────────────────────

def index(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Faça login para enviar uma avaliação.')
            return redirect('login')
        try:
            db.collection('avaliacao').add({
                'cliente': request.user.username,
                'comentario': request.POST.get('comentario', ''),
                'nota': int(request.POST.get('nota', 5)),
                'produto': request.POST.get('produto', ''),
            })
            messages.success(request, 'Avaliação enviada!')
        except Exception:
            messages.error(request, 'Erro ao salvar avaliação.')

    avaliacoes = []
    try:
        docs = db.collection('avaliacao').stream()
        for doc in docs:
            dados = doc.to_dict()
            dados['id'] = doc.id
            avaliacoes.append(dados)
    except Exception:
        pass

    return render(request, 'index.html', {'avaliacoes': avaliacoes})


def quemSomos(request):
    usuarios = User.objects.filter(is_staff=True)[:6]
    return render(request, 'quem-somos.html', {'usuarios': usuarios})


def loja(request):
    produtos = Produto.objects.all()
    try:
        response = requests.get('https://fakestoreapi.com/products', timeout=5)
        produtos_api = response.json()
    except Exception:
        produtos_api = []
    return render(request, 'loja.html', {
        'produtos': produtos,
        'produtos_api': produtos_api,
    })

def produto(request):
    print("ENTREI NA VIEW PRODUTO")

    produtos = Produto.objects.all()

    try:
        response = requests.get('https://fakestoreapi.com/products', timeout=5)
        produtos_api = response.json()
        print("API:", len(produtos_api))
    except Exception as e:
        print("ERRO:", e)
        produtos_api = []

    return render(request, 'produto.html', {
        'produtos': produtos,
        'produtos_api': produtos_api,
    })
    
def addContato(request):
    formulario = FormContato(request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        messages.success(request, 'Mensagem enviada! Entraremos em contato em breve.')
        return redirect('index')
    return render(request, 'add-contato.html', {'form': formulario})


# ─────────────────────────────────────
# Autenticação
# ─────────────────────────────────────

def cadastrarUsuario(request):
    if request.user.is_authenticated:
        return redirect('index')
    formulario = FormUsuario(request.POST or None)
    if request.method == 'POST':
        if formulario.is_valid():
            usuario = formulario.save()
            try:
                grupo = Group.objects.get(name='Cliente')
                usuario.groups.add(grupo)
            except Group.DoesNotExist:
                pass
            messages.success(request, 'Conta criada! Faça login.')
            return redirect('login')
    else:
        formulario = FormUsuario()
    return render(request, 'cadastro.html', {'form': formulario})


def loginUsuario(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos.'})
    return render(request, 'login.html')


def logoutUsuario(request):
    logout(request)
    return redirect('login')


# ─────────────────────────────────────
# Perfil do Cliente
# ─────────────────────────────────────

@login_required(login_url='login')
def perfil(request):
    compras = Compra.objects.filter(usuario=request.user).select_related('produto_db')
    return render(request, 'perfil.html', {'compras': compras})


@login_required(login_url='login')
def editarUsuario(request):
    formulario = FormEditarUsuario(request.POST or None, instance=request.user)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        messages.success(request, 'Perfil atualizado!')
        return redirect('perfil')
    return render(request, 'edit-usuario.html', {'form': formulario})


# ─────────────────────────────────────
# Compras
# ─────────────────────────────────────

@login_required(login_url='login')
def comprarProduto(request, id_prod):
    if request.method == 'POST':
        produto = get_object_or_404(Produto, id=id_prod)
        if produto.quantidade > 0:
            produto.quantidade -= 1
            produto.save()
            Compra.objects.create(
                usuario=request.user,
                produto_nome=produto.nome,
                produto_db=produto,
                valor=produto.preco,
                quantidade=1,
            )
            messages.success(request, f"✓ Compra de '{produto.nome}' realizada com sucesso!")
        else:
            messages.error(request, f"'{produto.nome}' está sem estoque.")
        return redirect('perfil')
    return redirect('loja')


@login_required(login_url='login')
def comprarProdutoApi(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', 'Produto')
        preco = request.POST.get('preco', '0')
        Compra.objects.create(
            usuario=request.user,
            produto_nome=nome,
            produto_db=None,
            valor=preco,
            quantidade=1,
        )
        messages.success(request, f"✓ Compra de '{nome}' realizada com sucesso!")
        return redirect('perfil')
    return redirect('loja')


@login_required(login_url='login')
def avaliarCompra(request, id_compra):
    compra = get_object_or_404(Compra, id=id_compra, usuario=request.user)
    if compra.avaliado:
        messages.info(request, 'Você já avaliou esta compra.')
        return redirect('perfil')
    if request.method == 'POST':
        comentario = request.POST.get('comentario', '')
        nota = int(request.POST.get('nota', 5))
        try:
            db.collection('avaliacao').add({
                'cliente': request.user.username,
                'produto': compra.produto_nome,
                'comentario': comentario,
                'nota': nota,
            })
        except Exception:
            pass
        compra.avaliado = True
        compra.save()
        messages.success(request, 'Avaliação enviada! Obrigado.')
        return redirect('perfil')
    return render(request, 'avaliacao.html', {'compra': compra})


# ─────────────────────────────────────
# Categoria (Admin)
# ─────────────────────────────────────

@staff_member_required
def listarCategoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria.html', {'categorias': categorias})


@staff_member_required
def addCategoria(request):
    formulario = FormCategoria(request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('categoria')
    return render(request, 'add-categoria.html', {'form': formulario})


@staff_member_required
def editCategoria(request, id_cat):
    categoria = get_object_or_404(Categoria, id=id_cat)
    formulario = FormCategoria(request.POST or None, instance=categoria)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('categoria')
    return render(request, 'edit-categoria.html', {'form': formulario})


@staff_member_required
def delCategoria(request, id_cat):
    get_object_or_404(Categoria, id=id_cat).delete()
    return redirect('categoria')


# ─────────────────────────────────────
# Contato (Admin)
# ─────────────────────────────────────

@staff_member_required
def listarContatoAdmin(request):
    contatos = Contato.objects.all().order_by('-id')
    return render(request, 'contato.html', {'contatos': contatos})


@staff_member_required
def delContato(request, id_contato):
    get_object_or_404(Contato, id=id_contato).delete()
    return redirect('contato')


# ─────────────────────────────────────
# Produto (Admin)
# ─────────────────────────────────────

@staff_member_required
def produto(request):
    produtos = Produto.objects.all().select_related('categoria')
    return render(request, 'produto.html', {'produtos': produtos})


@staff_member_required
def addProduto(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('produto')
    return render(request, 'addproduto.html', {'form': form})


@staff_member_required
def editProduto(request, id_prod):
    prod = get_object_or_404(Produto, id=id_prod)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=prod)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('produto')
    return render(request, 'edit-produto.html', {'form': form, 'produto': prod})


@staff_member_required
def delProduto(request, id_prod):
    get_object_or_404(Produto, id=id_prod).delete()
    return redirect('produto')


# ─────────────────────────────────────
# Dashboard (Admin)
# ─────────────────────────────────────

@staff_member_required
def dashboard(request):
    total_avaliacoes = 0
    try:
        total_avaliacoes = len(list(db.collection('avaliacao').stream()))
    except Exception:
        pass

    return render(request, 'dashboard.html', {
        'total_produtos':   Produto.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'total_contatos':   Contato.objects.count(),
        'total_usuarios':   User.objects.count(),
        'total_compras':    Compra.objects.count(),
        'total_avaliacoes': total_avaliacoes,
    })


# ─────────────────────────────────────
# Usuários (Admin)
# ─────────────────────────────────────

@staff_member_required
def listarUsuarios(request):
    usuarios = User.objects.all().order_by('date_joined')
    return render(request, 'usuarios.html', {'usuarios': usuarios})


@staff_member_required
def addUsuarioAdmin(request):
    formulario = FormUsuario(request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'add-usuario.html', {'form': formulario})


@staff_member_required
def editUsuarioAdmin(request, id_user):
    usuario = get_object_or_404(User, id=id_user)
    formulario = FormEditarUsuario(request.POST or None, instance=usuario)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'edit-usuario-admin.html', {'form': formulario, 'usuario': usuario})


@staff_member_required
def delUsuario(request, id_user):
    usuario = get_object_or_404(User, id=id_user)
    if not usuario.is_superuser:
        usuario.delete()
    return redirect('usuarios')


# ─────────────────────────────────────
# Compras (Admin)
# ─────────────────────────────────────

@staff_member_required
def listarComprasAdmin(request):
    compras = Compra.objects.all().select_related('usuario', 'produto_db').order_by('-data')
    return render(request, 'compras-admin.html', {'compras': compras})


@staff_member_required
def delCompraAdmin(request, id_compra):
    get_object_or_404(Compra, id=id_compra).delete()
    return redirect('comprasadmin')


# ─────────────────────────────────────
# Avaliações (Admin)
# ─────────────────────────────────────

@staff_member_required
def listarAvaliacoesAdmin(request):
    avaliacoes = []
    try:
        docs = db.collection('avaliacao').stream()
        for doc in docs:
            dados = doc.to_dict()
            dados['id'] = doc.id
            avaliacoes.append(dados)
    except Exception:
        pass
    return render(request, 'avaliacoes-admin.html', {'avaliacoes': avaliacoes})

@staff_member_required
def editarAvaliacaoAdmin(request, id_avaliacao):

    avaliacao_ref = db.collection('avaliacao').document(id_avaliacao)

    try:
        avaliacao = avaliacao_ref.get().to_dict()

    except Exception:
        messages.error(request, 'Avaliação não encontrada.')
        return redirect('avaliacoesadmin')

    if request.method == 'POST':

        novos_dados = {
            'cliente': request.POST.get('cliente'),
            'produto': request.POST.get('produto'),
            'comentario': request.POST.get('comentario'),
            'nota': int(request.POST.get('nota')),
        }

        avaliacao_ref.update(novos_dados)

        messages.success(request, 'Avaliação atualizada com sucesso!')
        return redirect('avaliacoesadmin')

    return render(request, 'editar-avaliacao.html', {
        'avaliacao': avaliacao,
        'id_avaliacao': id_avaliacao
    })

@staff_member_required
def delAvaliacaoAdmin(request, id_avaliacao):
    try:
        db.collection('avaliacao').document(id_avaliacao).delete()
    except Exception:
        pass
    return redirect('avaliacoes-admin')
