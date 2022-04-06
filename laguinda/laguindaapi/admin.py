from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Producto, Ingrediente, Valoracion, Oferta, Comentario, Tienda
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

admin.site.register(Producto)
admin.site.register(Ingrediente)
admin.site.register(Valoracion)
admin.site.register(Oferta)
admin.site.register(Comentario)
admin.site.register(Tienda)
