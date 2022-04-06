from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields

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
    media = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return self.nombre
        
class Comentario(models.Model):
    valoproduc = models.ForeignKey('Producto', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)

    def __str__(self):
        return  (str(self.user)+" "+self.valoproduc.nombre)

class Valoracion(models.Model):
    valoproduc = models.ForeignKey('Producto', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(choices=PUNTUACION)

    def __str__(self):
        return str(self.puntuacion)

class Tienda(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
        
#https://www.google.com/maps/place/Pasteler%C3%ADa+La+Guinda/@36.471586,-6.1922979,19.29z/data=!4m8!1m2!2m1!1sgeolocalizacion!3m4!1s0xd0dcce08c134d7b:0xecc88bd08d92e28b!8m2!3d36.4717928!4d-6.1922364