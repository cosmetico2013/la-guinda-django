from django.contrib import admin
from .models import Usuario, Producto, Ingredientes, Valoraciones, Componentes

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Ingredientes)
admin.site.register(Valoraciones)
admin.site.register(Componentes)