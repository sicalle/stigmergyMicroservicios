from django.shortcuts import render
from .logic.usuarios_logic import get_all_usuarios
from .logic.usuarios_logic import get_usuario_db
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

def get_usuarios(request):
    usuarios = get_all_usuarios()
    usuarios_list = serializers.serialize('json', usuarios)

    return render(
        request,
        'indexO_list.html',
        context = {"usuarios":usuarios}
        )

def get_usuario(request, pk=1):

    context = {}
    system = request.POST.get("system", None)
    x = system
    usuario = get_usuario_db(x)

    usuario_seria = serializers.serialize('json', [usuario])
    return render(
        request,
        'indexO_get.html',
        context = {"usuario":usuario}
        )