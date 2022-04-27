from django.db import models
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

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    Fecha_Pedido = models.DateTimeField(blank=True, null=True)
    Fecha_Entrega = models.DateTimeField(blank=True, null=True)
    Fecha_Terminado = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.user) +" "+ str(self.Fecha_Pedido)

class Encargo(models.Model):
    reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=3,decimal_places=0, default=0)
    costo = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return str(self.reserva)+" "+ str(self.producto)+" "+ str(self.cantidad)