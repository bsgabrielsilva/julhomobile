from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def autenticacao(request, template_name="login.html"):
    if not request.user.is_authenticated and not request.user.is_staff:
        next = request.GET.get('next', '/')
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                messages.error(request, "Usuário e/ou Senha incorretos.")
                return HttpResponseRedirect(settings.LOGIN_URL)
        return render(request, template_name, {'redirect_to': next})
    else:
        return redirect('painel_administrativo')


def sair(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)
