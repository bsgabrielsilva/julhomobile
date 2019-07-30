from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def home(request, template_name="home.html"):
    if request.user.is_staff:
        return render(request, template_name)
    else:
        messages.error(request, "Você não tem permissão para acessar isso.")
        return redirect('sair')