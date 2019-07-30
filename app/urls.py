from django.urls import path
from .views import *

urlpatterns = [
    path('login/', autenticacao, name="login"),
    path('sair/', sair, name="sair"),
    path('', postagens, name="postagens"),
    path('post/<int:pk>', postagem, name="postagem"),
    path('home/', home, name="home"),

    path('posts/', home_post, name="home_posts"),
    path('posts/cadastrar', cadastrar_post, name="cadastrar_post"),
    path('posts/editar/<int:pk>', editar_post, name="editar_post"),
    path('posts/remover/<int:pk>', remover_post, name="remover_post")
]