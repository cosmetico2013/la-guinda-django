from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls.base import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from laguindaapi.models import Producto, Comentario, Valoracion, Tienda
from django.db.models import Q
from django.core.exceptions import PermissionDenied
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
    permission_required='laguindaapi.add_Producto'

class ProductoUpdateView(PermissionRequiredMixin,UpdateView):
    model = Producto
    success_url= reverse_lazy("producto-list")
    fields = ['nombre','precio','oferta','imagen','ingrediente']
    template_name_suffix = '_update_form'
    permission_required='laguindaapi.change_Producto'

class ProductoDeleteView(PermissionRequiredMixin,DeleteView):
    model = Producto
    success_url = reverse_lazy('producto-list')
    permission_required='laguindaapi.delete_Producto'

class ProductoDetailView(DetailView):
    model = Producto
    def get_object(self):
        obj = super().get_object()
        valos= obj.valoracion_set.all()
        if len(valos) != 0:
            cuenta=0
            for punto in valos:
                cuenta+=int(punto.puntuacion)
            if not obj.media == int(cuenta)/len(valos):
                obj.media = int(cuenta)/len(valos)
                obj.save()
                obj=Producto.objects.get(nombre=obj)
        sale=obj
        return sale
    def get_context_data(self, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            list = Valoracion.objects.filter(user=self.request.user, valoproduc=super().get_object())
            if len(list) == 0:
                context['valorado'] = False
            else:   
                context['valorado'] = True
        #return super().get_context_data(**kwargs)
        return context


# vistas para comentarios
class ComentarioDetailView(DetailView):
    model = Comentario

class ComentarioCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Comentario
    fields = ['texto']
    def form_valid(self, form):
        url=self.request.get_full_path()
        urllist=url.split("/")
        objeto=Producto.objects.get(pk=int(urllist[3]))
        form.instance.valoproduc = objeto
        form.instance.user = self.request.user
        form.save()
        return redirect('producto-detail', pk=urllist[3])

class ComentarioUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Comentario
    fields = ['texto']
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        if form.instance.user == self.request.user or self.request.user.is_staff:
            form.save()
            return redirect('producto-detail', pk=form.instance.valoproduc.pk)
        else:
            raise PermissionDenied

class ComentarioDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Comentario
    success_url = reverse_lazy('producto-list')


# vistas para Valoraciones
class ValoracionDetailView(DetailView):
    model = Valoracion

class ValoracionCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Valoracion
    fields = ['puntuacion']
    def form_valid(self, form):
        url=self.request.get_full_path()
        urlcad=url.split("/")
        objeto=Producto.objects.get(pk=int(urlcad[3]))
        form.instance.valoproduc = objeto
        form.instance.user = self.request.user
        list = Valoracion.objects.filter(user=self.request.user, valoproduc=objeto)
        if len(list) == 0:
            form.save()
            return redirect('producto-detail', pk=urlcad[3])
        else:
            raise PermissionDenied
    def get_context_data(self, **kwargs):
        url=self.request.get_full_path()
        urlcad=url.split("/")
        objeto=Producto.objects.get(pk=int(urlcad[3]))
        context = super(ValoracionCreateView, self).get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            list = Valoracion.objects.filter(user=self.request.user, valoproduc=objeto)
            if len(list) == 0:  
                context['valorado'] = False
            else:   
                context['valorado'] = True
        #return super().get_context_data(**kwargs)
        return context

class ValoracionUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Valoracion
    fields = ['puntuacion']
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        if form.instance.user == self.request.user or self.request.user.is_staff:
            form.save()
            return redirect('producto-detail', pk=form.instance.valoproduc.pk)
        else:
            raise PermissionDenied

class ValoracionDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Valoracion
    success_url= reverse_lazy("producto-list")
    

# busqueda para productos
class Search_producto(ListView):
    model = Producto
    Template_name = 'search_producto.html'
    def get_queryset (self):
        query = self.request.GET.get("q")
        object_list = Producto.objects.filter( Q (nombre__icontains=query))
        return object_list


#tienda
class TiendaListView(ListView):
    model = Tienda