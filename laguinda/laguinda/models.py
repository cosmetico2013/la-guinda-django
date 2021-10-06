from settings import BASE_DIR
from django.db import models

class Usuario(models.Model):
    nomusu = models.CharField(max_length=50)
    apeusu = models.CharField(max_length=100)
    correousu = models.EmailField()

class Producto (models.Model):
    nomproduc = models.CharField(max_length=50)
    precioprodu = models.BigAutoField()
    oferta = models.CharField(max_length=100)
    imagen = models.FilePathField(path=BASE_DIR)

class Ingredientes(models.Model):
    nomingre = models.CharField()

class Valoraciones(models.Model):
    puntuacion = models.BigAutoField()
    comentario = models.CharField(max_length=500)

class Componentes(models.Model):
    cantidad = models.BigAutoField()