from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Usuario, Producto, Ingrediente, Valoracion, Componente, Oferta

class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural="usuarios"

class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioInline,)


admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Ingrediente)
admin.site.register(Valoracion)
admin.site.register(Componente)
admin.site.register(Oferta)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)