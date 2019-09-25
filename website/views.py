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

        args = {
            'msg': 'Até quem fim meus programas estão dando certo Uhuuuuuuuuuuuuuuu'
        }
        return render(request, 'index.html', args)
    
    return render(request, 'index.html')

