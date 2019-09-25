from django.shortcuts import render
from website.models import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        coach = Coach()
        coach.nome = request.POST['nome']
        coach.frase = request.POST['frase']
        coach.inspirador = request.POST['inspirador']
        coach.save()

        args = { ## Passando a msg de retorno quando o cliente enviar o formulário
            'msg': 'Até quem fim meus programas estão dando certo Uhuuuuuuuuuuuuuuu'
        }
        return render(request, 'index.html', args) ## Passando o retorno para o index
    
    return render(request, 'index.html')

def listar_coachs(request):
    listar_coachs = Coach.objects.all()
    args = {
        'listar_coachs': listar_coachs
    }
    return render(request, 'listar_coachs.html', args)
