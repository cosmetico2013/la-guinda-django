from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User


PUNTUACION=[(1,1),(2,2),(3,3),(4,4),(5,5)]

actual= timezone.now()

class Oferta(models.Model):
    cantidad = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    precio = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return str(self.cantidad)+' x '+str(self.precio)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    oferta = models.ForeignKey('Oferta',on_delete=models.SET_NULL ,blank=True, null=True)
    ingrediente = models.ManyToManyField('Ingrediente')
    imagen = models.FileField(upload_to="img/")

    def __str__(self):
        return self.nombre
        
class Comentario(models.Model):
    valoproduc = models.ForeignKey('Producto', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cabecera= models.CharField(max_length=100)
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.cabecera

class Valoracion(models.Model):
    valoproduc = models.ForeignKey('Producto', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(choices=PUNTUACION)

    def __str__(self):
        return str(self.puntuacion)
