from django.shortcuts import get_object_or_404, redirect, render # type: ignore
from musicass.forms import Musicasform
from musicass.models import Musicas

def listar_musicas(request):
    musica = Musicas.objects.all()
    return render(request, 'listarmusicas.html', {'musica': musica})

def cadastrar_musicas(request):
    if request.method == "POST":
        form = Musicasform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_musicas')
    else:
        form = Musicasform()
    return render(request, 'formmusica.html', {'form': form})

def editar_musicas(request, id):
    musicas = get_object_or_404(Musicas, id=id)
    if request.method == "POST":
        form = Musicasform(request.POST, instance=musicas)
        if form.is_valid():
            form.save()
            return redirect('listar_musicas')
    else:
        form = Musicasform(instance=musicas)
    return render(request, 'formmusica.html', {'form': form})

def excluir_musicas(request, id):
    musicas = get_object_or_404(Musicas, id=id)
    if request.method == 'POST':
        musicas.delete()
        return redirect('listar_musicas')
    return render(request, 'excluirmusica.html', {'musicas': musicas})
