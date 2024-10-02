from django.shortcuts import get_object_or_404, render, redirect # type: ignore
from .models import Music

def listar_music(request):
    musiquinha = Music.objects.all()  # Obtém todas as músicas do banco de dados
    return render(request, 'list_music.html', {'musicas': musiquinha})

def cadastrar_music(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        Music.objects.create(nome=nome)
        return redirect('listar_music')
    return render(request, 'form_music.html')

def editar_music(request, id):
    musica = get_object_or_404(Music, id=id)
    if request.method == 'POST':
        musica.nome = request.POST['nome']
        musica.save()
        return redirect('listar_music')
    return render(request, 'form_music.html', {'musica': musica})

def excluir_musica(request, id):
    musica = get_object_or_404(Music, id=id)
    if request.method == 'POST':
        musica.delete()
        return redirect('listar_music')
    return render(request, 'del_music.html', {'musica': musica})