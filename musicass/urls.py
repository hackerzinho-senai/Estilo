from django.urls import path # type: ignore
from musicass.views import listar_musicas, cadastrar_musicas, editar_musicas, excluir_musicas

urlpatterns = [
    path('', listar_musicas, name='listar_musicas'),
    path('musicas/cadastrar/', cadastrar_musicas, name='cadastrar_musicas'),
    path('musicas/editar/<int:id>/', editar_musicas, name='editar_musicas'),
    path('musicas/excluir/<int:id>/', excluir_musicas, name='excluir_musicas'),
]

