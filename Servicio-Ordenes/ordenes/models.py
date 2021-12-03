from django.db import models
from django_cryptography.fields import encrypt

class Orden(models.Model):
    
    nameO = encrypt(models.CharField(max_length=50))
    valueO = encrypt(models.FloatField(null=True, blank=True, default=None))
    productosO = encrypt(models.CharField(max_length=50))
    tipoO = encrypt(models.CharField(
        max_length=50,
        choices=[("Medicina","Medicina"), ("Comida","Comida"), ("Basicos","Basicos")]  # some list of choices
        ))
    statusO = encrypt(models.CharField(
       max_length=50,
       choices=[("En Hub de despacho","En Hub de despacho"), ("Volando","Volando"), ("En Hub de llegada","En Hub de llegada")]  # some list of choices
       ))
    urlO = encrypt(models.CharField(max_length=500))
    dateTimeO = encrypt(models.DateTimeField(auto_now_add=True))
    
    def __str__(self):
        return '{0}'.format(self.nameO)
