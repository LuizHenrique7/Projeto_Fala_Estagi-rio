from django.shortcuts import render

from .models import Estagiario


def home(request):

    lista_post = Estagiario.objects.all()

    if request.method == 'POST':
        estagiario = Estagiario()
        estagiario.nome = request.POST.get("nome")
        estagiario.postagem = request.POST.get("postagem")
        estagiario.data = request.POST.get("data")
        estagiario.save()


    lista_ordenada = sorted(lista_post, key=lambda estagiario: estagiario.data)


    return render(request, 'home.html', {'lista_ordenada':lista_ordenada})

