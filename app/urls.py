from django.urls import path
from .views import autenticacao, sair, home, home_post, editar_post, cadastrar_post

urlpatterns = [
    path('login/', autenticacao, name="login"),
    path('sair/', sair, name="sair"),
    path('', home, name="home"),

    path('posts/', home_post, name="home_posts"),
    path('posts/cadastrar', cadastrar_post, name="cadastrar_post"),
    path('posts/editar/<int:pk>', editar_post, name="editar_post")
]