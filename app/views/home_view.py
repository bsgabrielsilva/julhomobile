from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Post
from ..forms import CommentsForm


@login_required
def home(request, template_name="home.html"):
    if request.user.is_staff:
        return render(request, template_name)
    else:
        messages.error(request, "Você não tem permissão para acessar isso.")
        return redirect('sair')


def postagens(request, template_name="publico/home.html"):
    posts = Post.objects.filter(status="Publicado").order_by('-created')
    return render(request, template_name, {'posts': posts})


def postagem(request, pk, template_name="publico/postagem.html"):
    post = get_object_or_404(Post, pk=pk)
    form = None
    if request.user.is_authenticated:
        form = CommentsForm(request.POST or None, initial={'post': post.pk})
        if request.method == "POST":
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.user = request.user
                comentario.save()
                messages.success(request, "comentário enviado com sucesso! Aguarde autorização!")
                return redirect('postagens')

    return render(request, template_name, {'form': form, 'post': post})