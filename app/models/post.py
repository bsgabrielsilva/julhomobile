from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS = (
        ('Arquivado', 'Arquivado'),
        ('Publicado', 'Publicado'),
        ('Rascunho', 'Rascunho')
    )
    titulo = models.CharField("Título", max_length=150, null=False)
    status = models.CharField("Situação", max_length=20, choices=STATUS, null=False, default='Rascunho')
    corpo = models.TextField("Corpo", null=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo