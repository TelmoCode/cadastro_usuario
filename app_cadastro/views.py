from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # Salva os usuarios no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibe todos os usuarios cadastrados em uma nova pagina
    usuarios = [
        'usuarios': Usuario.object.all()
    ]
    # Retornar os dados para a pagina de listagem