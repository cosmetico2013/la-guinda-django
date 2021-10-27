from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from laguindaapi.models import Usuario, Oferta ,Producto, Ingrediente, Valoracione, Componente

# Create your views here.
class ProductoListView(ListView):
    model = Producto

class ProductoCreateView(PermissionRequiredMixin,CreateView):
    model = Producto
    fields = ['nombre','precio','oferta']
    permission_required='laguindaapi.add_choice'

class ProductoUpdateView(PermissionRequiredMixin,UpdateView):
    model = Producto
    fields = ['nombre','precio','oferta']
    template_name_suffix = '_update_form'
    permission_required='laguindaapi.change_choice'

class ProductoDeleteView(PermissionRequiredMixin,DeleteView):
    model = Producto
    success_url = reverse_lazy('producto-list')
    permission_required='laguindaapi.delete_choice'

class ProductoDetailView(DetailView):
    model = Producto

