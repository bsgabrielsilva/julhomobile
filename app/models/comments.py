from django.db import models
from django.contrib.auth.models import User


class Comments(models.Model):
    comment = models.TextField('Comentário', null=False)
    autorizado = models.BooleanField('Autorizado?', null=False, default=False)

    post = models.ForeignKey('app.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment