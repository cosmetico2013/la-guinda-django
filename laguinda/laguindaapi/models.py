from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    correo = models.EmailField()
    
    def __str__(self):
        return self.correo

class Oferta(models.Model):
    cantidad = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    precio = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return str(self.cantidad)+' x '+str(self.precio)

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    oferta = models.ForeignKey('Oferta', on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="img/")

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Valoracion(models.Model):
    valoproduc = models.ForeignKey('Producto', on_delete=models.CASCADE)
    valousu = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    cabecera= models.CharField(max_length=100)
    puntuacion = models.DecimalField(max_digits=5, decimal_places=0)
    comentario = models.CharField(max_length=500)
#    fecha_publicacion = models.TimeField(default=)

    def __str__(self):
        return self.cabecera

class Componente(models.Model):
    compoingre = models.ForeignKey('Ingrediente', on_delete=models.CASCADE)
    compoprodu = models.ForeignKey('Producto', on_delete=models.CASCADE)
#    orden = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return str(self.compoprodu)+": "+str(self.compoingre)
