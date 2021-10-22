from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from laguindaapi.models import Usuario, Oferta ,Producto, Ingrediente, Valoracione, Componente

# Create your views here.
class ProductoListView(ListView):
    model = Producto

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre','precio','oferta']

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre','precio','oferta']
    template_name_suffix = '_update_form'

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto-list')

class ProductoDetailView(DetailView):
    model = Producto

