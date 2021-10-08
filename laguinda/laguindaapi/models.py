from laguinda.settings import BASE_DIR
from django.db import models

class Usuario(models.Model):
    nomusu = models.CharField(max_length=50)
    apeusu = models.CharField(max_length=100)
    correousu = models.EmailField()

class Producto(models.Model):
    nomproduc = models.CharField(max_length=50)
    precioprodu = models.DecimalField(max_digits=100, decimal_places=2)
    oferta = models.CharField(max_length=100, null=True)
    imagen = models.FilePathField(path=BASE_DIR)

class Ingredientes(models.Model):
    nomingre = models.CharField(max_length=100)

class Valoraciones(models.Model):
    valoproduc = models.ForeignKey('Producto', on_delete=models.Case)
    valousu = models.ForeignKey('Usuario', on_delete=models.Case)
    puntuacion = models.DecimalField(max_digits=5, decimal_places=0)
    comentario = models.CharField(max_length=500)

class Componentes(models.Model):
    compoingre = models.ForeignKey('Ingredientes', on_delete=models.Case)
    compoprodu = models.ForeignKey('Producto', on_delete=models.Case)
