from django.shortcuts import render, redirect

def sistema_home(request):
    return render(request, 'estoque/paginainicial.html')

def sistema_homecss(request):
    return render(request, 'estoque/paginainicial.css')

def index_view(request):
    return render(request, 'estoque/index.html')