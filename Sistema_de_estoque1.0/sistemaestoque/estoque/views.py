from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemEstoqueForm
from .models import ItemEstoque,  Item, Movimentacao
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

def estoque_home(request):
    contexto = {
        "nome":"Usuário",
        "itens": ItemEstoque.objects.all()
    }
    return render(request, 'estoque/home.html', contexto)

def estoque_adicionar(request:HttpRequest):
    if request.method == "POST":
        formulario = ItemEstoqueForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("estoque:home")

    contexto = {
        "form": ItemEstoqueForm()
    }
    return render(request, 'estoque/adicionar.html' , contexto)

def estoque_remover(request:HttpRequest, id:int):
    item = get_object_or_404(ItemEstoque, id=id)
    item.delete()
    return redirect("estoque:home")

def estoque_editar(request:HttpRequest, id:int):
    item = get_object_or_404(ItemEstoque, id=id)
    if request.method == "POST":
        formulario = ItemEstoqueForm(request.POST, instance=item)
        if formulario.is_valid():
            formulario.save()
            return redirect("estoque:home")
        
    formulario = ItemEstoqueForm(instance=item)
    contexto = {
        "form": formulario
    }
    return render(request, 'estoque/editar.html', contexto)

def registrar_entrada(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        quantidade = int(request.POST.get("quantidade"))
        Movimentacao.objects.create(item=item, tipo="entrada", quantidade=quantidade)
        return redirect("home")

    return render(request, "estoque/adicionar.html", {"item": item})

def registrar_saida(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        quantidade = int(request.POST.get("quantidade"))

        if quantidade > item.estoque_total:
            return render(request, "estoque/editar.html", {
                "item": item,
                "erro": "Saída maior que o estoque disponível."
            })

        Movimentacao.objects.create(item=item, tipo="saida", quantidade=quantidade)
        return redirect("home")

    return render(request, "estoque/editar.html", {"item": item})

def historico(request):
    movimentacoes = Movimentacao.objects.select_related('item').order_by('-data')
    return render(request, "estoque/relatorio.html", {"movimentacoes": movimentacoes})

def pagina_social(request):
    return render(request, 'estoque/4JMteam.html')

