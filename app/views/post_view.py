from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import PostForm
from ..models import Post


@login_required
def cadastrar_post(request, template_name="posts/cadastrar.html"):
    try:
        form = PostForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, "Post criado com sucesso")
                return redirect('home_posts')
    except Exception:
        messages.error(request, "Erro ao cadastrar Post!")
    return render(request, template_name, {'form': form})


@login_required
def editar_post(request, pk, template_name="posts/cadastrar.html"):
    try:
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                posts = form.save(commit=False)
                posts.user = request.user
                posts.save()
                messages.success(request, "Post atualizado com sucesso.")
                return redirect('home_posts')
        else:
            form = PostForm(instance=post)
    except Exception:
        messages.error(request, "Erro ao atualizar serviço.")
    return render(request, template_name, {'form': form})


@login_required
def home_post(request, template_name="posts/home.html"):
    try:
        lista = Post.objects.all()
    except Exception:
        messages.error(request, "Erro ao acessar home.")
    return render(request, template_name, {'lista': lista})


@login_required
def remover_post(request, pk):
    if request.user.is_staff:
        try:
            post = get_object_or_404(Post, pk=pk)
            post.delete()
            messages.success(request, "Post removido com sucesso")
        except Exception:
            messages.error(request, "Não possível remover Post!")
        return redirect('home_posts')
