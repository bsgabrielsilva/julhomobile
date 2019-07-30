from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import CommentsAdminForm
from ..models import Comments

@login_required
def editar_comments(request, pk, template_name="comments/editar.html"):
    try:
        comments = get_object_or_404(Comments, pk=pk)
        if request.method == 'POST':
            form = CommentsAdminForm(request.POST, instance=comments)
            if form.is_valid():
                posts = form.save(commit=False)
                posts.user = request.user
                posts.save()
                messages.success(request, "Comentário atualizado com sucesso.")
                return redirect('home_comments')
        else:
            form = CommentsAdminForm(instance=comments)
    except Exception:
        messages.error(request, "Erro ao atualizar comments.")
    return render(request, template_name, {'form': form})


@login_required
def home_comments(request, template_name="comments/home.html"):
    try:
        lista = Comments.objects.filter(autorizado=False)
    except Exception:
        messages.error(request, "Erro ao acessar home.")
    return render(request, template_name, {'lista': lista})