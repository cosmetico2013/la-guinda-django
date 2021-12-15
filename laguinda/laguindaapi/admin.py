from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Producto, Ingrediente, Valoracion, Oferta, Comentario


admin.site.register(Producto)
admin.site.register(Ingrediente)
admin.site.register(Valoracion)
admin.site.register(Oferta)
admin.site.register(Comentario)
