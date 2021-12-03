from ..models import Usuario


def get_all_usuarios():
    usuarios = Usuario.objects.all()
    return usuarios

def get_usuario_db(n):
    usuario = Usuario.objects.get(pk=n)
    return usuario