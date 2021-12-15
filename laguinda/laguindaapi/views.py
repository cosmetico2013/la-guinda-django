from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from laguindaapi.models import Producto, Comentario, Valoracion

# vistas para index

def index(request):
      return render(request,'laguindaapi/index.html')


# vistas para productos
class ProductoListView(ListView):
    model = Producto

class ProductoCreateView(PermissionRequiredMixin,CreateView):
    model = Producto
    success_url= reverse_lazy("producto-list")
    fields = ['nombre','precio','oferta','imagen','ingrediente']
    permission_required='laguindaapi.add_choice'

class ProductoUpdateView(PermissionRequiredMixin,UpdateView):
    model = Producto
    success_url= reverse_lazy("producto-list")
    fields = ['nombre','precio','oferta','imagen','ingrediente']
    template_name_suffix = '_update_form'
    permission_required='laguindaapi.change_choice'

class ProductoDeleteView(PermissionRequiredMixin,DeleteView):
    model = Producto
    success_url = reverse_lazy('producto-list')
    permission_required='laguindaapi.delete_choice'

class ProductoDetailView(DetailView):
    model = Producto


# vistas para comentarios
class ComentarioListView(ListView):
    model = Comentario

class ComentarioDetailView(DetailView):
    model = Comentario

class ComentarioCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
#    redirect_field_name = 'redirect_to'
    success_url= reverse_lazy("comentario-list")
    model = Comentario
    fields = ['valoproduc','cabecera','texto']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ComentarioUpdateView(PermissionRequiredMixin,UpdateView):
    model = Comentario
    success_url= reverse_lazy("comentario-list")
    fields = ['valoproduc','cabecera','texto']
    template_name_suffix = '_update_form'
    permission_required='laguindaapi.change_choice'

class ComentarioDeleteView(PermissionRequiredMixin,DeleteView):
    model = Comentario
    success_url = reverse_lazy('comentario-list')
    permission_required='laguindaapi.delete_choice'

# vistas para Valoraciones
class ValoracionListView(ListView):
    model = Valoracion

class ValoracionDetailView(DetailView):
    model = Valoracion

class ValoracionCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    #redirect_field_name = 'redirect_to'
    success_url= reverse_lazy("valoracion-list")
    model = Valoracion
    fields = ['valoproduc','puntuacion']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ValoracionUpdateView(PermissionRequiredMixin,UpdateView):
    model = Valoracion
    success_url= reverse_lazy("valoracion-list")
    fields = ['valoproduc','puntuacion']
    template_name_suffix = '_update_form'
    permission_required='laguindaapi.change_choice'

class ValoracionDeleteView(PermissionRequiredMixin,DeleteView):
    model = Valoracion
    success_url = reverse_lazy('comentario-list')
    permission_required='laguindaapi.delete_choice'
