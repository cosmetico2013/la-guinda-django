from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Producto, Ingrediente, Valoracion, Oferta, Comentario, Tienda, Encargo, Reserva, Componente, Alergenos

admin.site.register(Producto)
admin.site.register(Ingrediente)
admin.site.register(Valoracion)
admin.site.register(Oferta)
admin.site.register(Comentario)
admin.site.register(Tienda)
admin.site.register(Encargo)
admin.site.register(Reserva)
admin.site.register(Componente)
admin.site.register(Alergenos)