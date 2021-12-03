from ..models import Orden

def get_all_ordenes():
    ordenes = Orden.objects.all()
    return ordenes

def get_orden_db(n):
    orden = Orden.objects.get(pk=n)
    return orden

def update_orden_db(n, new_value):
    orden = Orden.objects.get(pk=n)
    orden.statusO = new_value
    orden.save()
    return orden

def create_orden_db(pName, pValue, pProductos, pTipo, pStatus, pUrl):
    orden = Orden.objects.create(nameO=pName, valueO=pValue, productosO= pProductos, tipoO=pTipo, statusO=pStatus, urlO = pUrl)
    orden.save()
    return orden

def get_ordenes_priorizadas_db():
    ordenes = Orden.objects.all()
    return ordenes
