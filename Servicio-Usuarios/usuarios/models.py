from django.db import models
from django_cryptography.fields import encrypt

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = encrypt(models.CharField(max_length=50))
    correo = encrypt(models.CharField(max_length=50))
    fechaIns = models.DateTimeField()
    cantidadPedidos = models.IntegerField()
    tipo = encrypt(models.CharField(
        max_length=50,
        choices=[("Regular","Regular"), ("Premium","Premium")]  # some list of choices
        ))

    foto = encrypt(models.CharField(max_length=500))
    
    def __str__(self):
        return '{0}'.format(self.usuario)
