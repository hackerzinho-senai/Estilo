from django.db import models # type: ignore
from estilo.models import Music

class Musicas(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    estilo = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
