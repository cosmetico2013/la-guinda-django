from django.utils import timezone
from django.views.generic import ListView, DetailView
from laguindaapi.models import Usuario, Oferta ,Producto, Ingrediente, Valoracione, Componente

# Create your views here.
class ProductoListView(ListView):
    model = Producto

class ProductoDetailView(DetailView):
    model = Producto