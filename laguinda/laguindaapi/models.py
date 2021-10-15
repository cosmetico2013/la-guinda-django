from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
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
    oferta = models.ForeignKey('Oferta', on_delete=models.Case)
    imagen = models.FileField(upload_to="imagenes/")

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Valoracione(models.Model):
    valoproduc = models.ForeignKey('Producto', on_delete=models.Case)
    valousu = models.ForeignKey('Usuario', on_delete=models.Case)
    puntuacion = models.DecimalField(max_digits=5, decimal_places=0)
    comentario = models.CharField(max_length=500)
#    fecha_publicacion = models.TimeField(default=)

    def __str__(self):
        return self.puntuacion

class Componente(models.Model):
    compoingre = models.ForeignKey('Ingrediente', on_delete=models.Case)
    compoprodu = models.ForeignKey('Producto', on_delete=models.Case)
    orden = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.orden