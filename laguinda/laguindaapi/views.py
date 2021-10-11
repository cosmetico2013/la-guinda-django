from os import name
from django.views.generic import ListView
from laguindaapi.models import Usuario, Oferta ,Producto, Ingrediente, Valoracione, Componente

# Create your views here.
class UsuarioListView(ListView):
    model = name