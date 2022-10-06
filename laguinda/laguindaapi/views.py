import math
from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from laguindaapi.models import Producto, Comentario, Valoracion, Tienda, Reserva, Encargo
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from tempus_dominus.widgets import DateTimePicker
# vistas para index

def index(request):
      return render(request,'laguindaapi/index.html')


# vistas para productos
class ProductoListView(ListView):
    model = Producto
    def get_queryset (self):
        object_list = Producto.objects.order_by("-media")
        return object_list

class ProductoCreateView(PermissionRequiredMixin,CreateView):
    model = Producto
    success_url= reverse_lazy("Producto-list")
    fields = ['nombre','precio','oferta','imagen','ingrediente']
    permission_required='laguindaapi.add_Producto'

class ProductoUpdateView(PermissionRequiredMixin,UpdateView):
    model = Producto
    success_url= reverse_lazy("Producto-list")
    fields = ['nombre','precio','oferta','imagen','ingrediente']
    template_name_suffix = '_update_form'
    permission_required='laguindaapi.change_Producto'

class ProductoDeleteView(PermissionRequiredMixin,DeleteView):
    model = Producto
    success_url = reverse_lazy('Producto-list')
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
        return redirect('Producto-detail', pk=urllist[3])

class ComentarioUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Comentario
    fields = ['texto']
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        if form.instance.user == self.request.user or self.request.user.is_staff:
            form.save()
            return redirect('Producto-detail', pk=form.instance.valoproduc.pk)
        else:
            raise PermissionDenied

class ComentarioDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Comentario
    success_url = reverse_lazy('Producto-list')


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
            return redirect('Producto-detail', pk=urlcad[3])
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
        return context

class ValoracionUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Valoracion
    fields = ['puntuacion']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        if obj.user == self.request.user or self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        if form.instance.user == self.request.user or self.request.user.is_staff:
            form.save()
            return redirect('Producto-detail', pk=form.instance.valoproduc.pk)
        else:
            raise PermissionDenied

class ValoracionDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Valoracion
    success_url= reverse_lazy("Producto-list")
    

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

#reserva
class ReservaListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model= Reserva
    def get_queryset (self):
        object_list = Reserva.objects.filter(user=self.request.user).order_by("-Fecha_Pedido")
        return object_list

class ReservaDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Reserva
    def get_object(self):
        obj = super().get_object()
        valos= obj.encargo_set.all()
        if len(valos) != 0:
            cuenta=0
            for encargo in valos:
                cuenta+=encargo.costo
            if not obj.costo == cuenta:
                obj.costo = cuenta
                obj.save()
                obj=Reserva.objects.get(id=obj.id)
        else:
            obj.costo=0
            obj.save()
        sale=obj
        return sale

class ReservaCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Reserva
    fields = []
    success_url= reverse_lazy("reserva-list")
    def form_valid(self, form):
        actual= timezone.now()
        form.instance.Fecha_Pedido = actual
        form.instance.user = self.request.user
        form.instance.costo = 0
        return super().form_valid(form)

class ResevaUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Reserva
    success_url= reverse_lazy("reserva-list")
    template_name_suffix = '_update_form'
    fields = ['Fecha_Entrega']
    def get_form(self):
        form = super().get_form()
        form.fields['Fecha_Entrega'].widget = DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
        return form
    def get_object(self):
        obj=super().get_object()
        if obj.user == self.request.user or self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        actual = timezone.now()
        days=timezone.datetime(actual.year,actual.month,actual.day+3,actual.hour+2,actual.minute,actual.second,actual.microsecond,actual.tzinfo)
        if type(form.instance.Fecha_Entrega) == type(days):
            if form.instance.Fecha_Entrega > days:
                return super().form_valid(form)
        form.add_error("Fecha_Entrega","Introduzca una fecha/hora válida.")
        return super().form_invalid(form)

class ReservaDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Reserva
    success_url= reverse_lazy("reserva-list")
    def get_object(self):
        obj=super().get_object()
        if obj.user == self.request.user or self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

#encargo
class EncargoCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Encargo
    fields = ['producto','cantidad']
    success_url= reverse_lazy("reserva-list")
    def form_valid(self, form):
        if form.instance.cantidad <= 0:
            form.add_error("cantidad","El valor no puede ser inferior o igual a 0.")
            return super().form_invalid(form)
        url=self.request.get_full_path()
        urlcad=url.split("/")
        objeto=Reserva.objects.get(pk=int(urlcad[3]))
        for encargo in objeto.encargo_set.all():
            if encargo.producto == form.instance.producto:
                form.add_error("producto","Usted ya tiene este producto en la reserva.")
                return super().form_invalid(form)
        form.instance.reserva = objeto
        list = Reserva.objects.filter(user=self.request.user, id=objeto.id)
        if len(list) == 1:
            cuenta=0
            if  form.instance.producto.oferta:
                opera = form.instance.cantidad/form.instance.producto.oferta.cantidad
                if math.floor(opera) == math.ceil(opera):
                    cuenta+=opera*form.instance.producto.oferta.precio
                else:
                    cuenta+=form.instance.producto.precio*(form.instance.cantidad-math.floor(opera)*form.instance.producto.oferta.cantidad)+math.floor(opera)*form.instance.producto.oferta.precio
            else:
                cuenta+=form.instance.cantidad*form.instance.producto.precio
            form.instance.costo=cuenta
            form.save()
            return redirect('reserva-detail', pk=urlcad[3])
        else:
            raise PermissionDenied
    def get_context_data(self, **kwargs):
        url=self.request.get_full_path()
        urlcad=url.split("/")
        objeto=Reserva.objects.get(pk=int(urlcad[3]))
        context = super(EncargoCreateView, self).get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            list = Reserva.objects.filter(user=self.request.user, id=objeto.id)
            if not len(list) == 1:
                raise PermissionDenied
        return context
    
class EncargoUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Encargo
    fields = ['cantidad']
    success_url= reverse_lazy("reserva-list")
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        if obj.reserva.user == self.request.user or self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        if form.instance.cantidad <= 0:
            form.add_error("cantidad","El valor no puede ser inferior o igual a 0.")
            return super().form_invalid(form)
        cuenta=0
        if  form.instance.producto.oferta:
            opera = form.instance.cantidad/form.instance.producto.oferta.cantidad
            if math.floor(opera) == math.ceil(opera):
                cuenta+=opera*form.instance.producto.oferta.precio
            else:
                cuenta+=form.instance.producto.precio*(form.instance.cantidad-math.floor(opera)*form.instance.producto.oferta.cantidad)+math.floor(opera)*form.instance.producto.oferta.precio
        else:
            cuenta+=form.instance.cantidad*form.instance.producto.precio
        form.instance.costo=cuenta
        form.save()
        return redirect('reserva-detail', pk=self.object.reserva.id)

class EncargoDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Encargo
    success_url= reverse_lazy("reserva-list")
    def get_object(self):
        obj=super().get_object()
        if obj.reserva.user == self.request.user or self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied
    def get_context_data(self, **kwargs):
        context = super(EncargoDeleteView, self).get_context_data(**kwargs)
        obj = super().get_object()
        if obj.reserva.Fecha_Entrega:
            context['entregado'] = True
        else:
            context['entregado'] = False
        return context

#Pendiente
class PendienteListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Reserva
    template_name_suffix = '_pendiente_list'
    def get_queryset (self):
        if self.request.user.is_staff:
            return Reserva.objects.order_by('Fecha_Entrega')
        else:
            raise PermissionDenied
    def get_context_data(self, **kwargs):
        context = super(PendienteListView, self).get_context_data(**kwargs)
        actual = timezone.now()
        days=timezone.datetime(actual.year,actual.month,actual.day-1,actual.hour,actual.minute,actual.second,actual.microsecond,actual.tzinfo)
        context['fecha'] = days
        return context

class PendienteUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Reserva
    fields = []
    template_name_suffix = '_pendiente_update'
    success_url= reverse_lazy("pendiente-list")
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        actual = timezone.now()
        if form.instance.Fecha_Terminado:
            form.instance.Fecha_Terminado=None
        else:
            form.instance.Fecha_Terminado=actual
        return super().form_valid(form)