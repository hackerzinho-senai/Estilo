# estilo/urls.py
from django.urls import path
from .views import listar_music, cadastrar_music, editar_music, excluir_musica

urlpatterns = [
    path('', listar_music, name='listar_music'),  # URL base para listar músicas
    path('cadastrar/', cadastrar_music, name='cadastrar_music'),  # URL para cadastrar música
    path('editar/<int:id>/', editar_music, name='editar_music'),  # URL para editar música
    path('excluir/<int:id>/', excluir_musica, name='excluir_musica'),  # URL para excluir música
]
