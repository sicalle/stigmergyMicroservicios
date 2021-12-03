from django.shortcuts import render
from .logic.ordenes_logic import get_all_ordenes
from .logic.ordenes_logic import get_orden_db
from .logic.ordenes_logic import update_orden_db
from .logic.ordenes_logic import create_orden_db
from .logic.ordenes_logic import get_ordenes_priorizadas_db
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

# Create your views here.
def get_ordenes(request):
    ordenes = get_all_ordenes()
    orden_list = serializers.serialize('json', ordenes)

    num_ordenes = ordenes.count()

    return render(
        request,
        'indexO_list.html',
        context = {"ordenes":ordenes}
        )


def get_orden(request, pk=1):

    context = {}
    system = request.POST.get("system", None)
    x = system
    orden = get_orden_db(x)

    orden_seria = serializers.serialize('json', [orden])
    return render(
        request,
        'indexO_get.html',
        context = {"orden":orden}
        )

@login_required
def update_orden(request, pk=1, new_value=100):
    role = getRole(request)
    print("Rol: " , role)
    if role == "Gerente":
        status = request.POST.get("status")
        if status == None:
            status = "Volando"
        pk1 = request.POST.get("pk1")
        if pk1 == None:
            pk1 = 2
        orden = update_orden_db(pk1, status)
        orden_seria = serializers.serialize('json', [orden])
    
        return render(
            request,
            'indexO_get.html',
            context = {"orden":orden}
            )
    else:
        return HttpResponse("Usuario no autorizado")
    

#def update_orden(request, pk=1, new_value=100):
#
#    status = request.POST.get("status")
#    pk1 = request.POST.get("pk1")
#
#    orden = update_orden_db(pk1, status)
#    orden_seria = serializers.serialize('json', [orden])
#
#    return render(
#        request,
#        'indexO_get.html',
#        context = {"orden":orden}
#        )

def create_orden(request):

    name = request.POST.get("name", None)
    value = request.POST.get("value", None)
    productos = request.POST.get("productos", None)
    tipo = request.POST.get("tipo", None)
    status = request.POST.get("status", None)
    url = request.POST.get("url", None)

    orden = create_orden_db(name, value, productos, tipo, status, url)

    orden_seria = serializers.serialize('json', [orden])
    return render(
        request,
        'indexO_get.html',
        context = {"orden":orden}
        )

def get_ordenes_priorizadas(request):
    ordPri = []
    ordenes = get_ordenes_priorizadas_db()

    for i in range(len(ordenes)):
        if ordenes[i].tipoO == "Medicina":
            ordPri.append(ordenes[i])
    for i in range(len(ordenes)):
        if ordenes[i].tipoO == "Comida":
            ordPri.append(ordenes[i])
    for i in range(len(ordenes)):
        if ordenes[i].tipoO == "Basicos":
            ordPri.append(ordenes[i])

    return render(
        request,
        'indexO_listPrio.html',
        context = {"ordenes":ordPri}
        )

