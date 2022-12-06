from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from laguindaapi import views
from laguindaapi.views import ProductoListView, ProductoDetailView, ProductoCreateView, ProductoDeleteView, ProductoUpdateView
from laguindaapi.views import ComentarioCreateView, ComentarioDeleteView, ComentarioUpdateView, ComentarioDetailView
from laguindaapi.views import ValoracionUpdateView, ValoracionDetailView, ValoracionCreateView, ValoracionDeleteView, TiendaListView
from laguindaapi.views import ReservaCreateView, ReservaListView, ReservaDetailView, ResevaUpdateView, ReservaDeleteView
from laguindaapi.views import EncargoCreateView, EncargoDeleteView, EncargoUpdateView
from laguindaapi.views import PendienteListView, PendienteUpdateView
from laguindaapi.views import Ingredientelistview, IngredienteDetailView, IngredienteCreateView, IngredienteUpdateView, IngredienteDeleteView
from laguindaapi.views import ComponenteListView, ComponenteDetailView, ComponenteCreateView, ComponenteUpdateview, ComponenteDeleteView
from laguindaapi.views import AleProductoListeview, AleProductoDetailview, AleProductoCreateView, AleProductoUpdateView, AleProductoDeleteView
from laguindaapi.views import Search_producto
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

from laguindaapi.models import Producto, Oferta, Ingrediente
from rest_framework import routers, viewsets, serializers

# contenido que proporciona la busqueda en la API
class OfertaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Oferta
        fields = ['cantidad', 'precio']

class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer


class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['nombre']

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'ingrediente', 'oferta','media']

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# url configuracion
router = routers.DefaultRouter()
router.register(r'producto-api', ProductoViewSet)
router.register(r'oferta-api', OfertaViewSet) 
router.register(r'ingrediente-api', IngredienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    #  urls para el index
    #path('', views.index, name='index.html'),
    path('sobre-nosotros/', TiendaListView.as_view(), name='sobre-nosotros'),

    #  urls para productos
    path('', ProductoListView.as_view(), name='Producto-list' ),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='Producto-detail'),
    path('producto/add/', ProductoCreateView.as_view(), name='Producto-add'),
    path('producto/<int:pk>/update/', ProductoUpdateView.as_view(), name='Producto-update'),
    path('producto/<int:pk>/delete/', ProductoDeleteView.as_view(), name='Producto-delete'),

    #  urls para comentarios
    path('comentario/<int:pk>/', ComentarioDetailView.as_view(), name='comentario-detail'),
    path('comentario/add/<int:pk>/', ComentarioCreateView.as_view(), name='comentario-add'),
    path('comentario/<int:pk>/update/', ComentarioUpdateView.as_view(), name='comentario-update'),
    path('comentario/<int:pk>/delete/', ComentarioDeleteView.as_view(), name='comentario-delete'),

    #  urls para valoraciones
    path('valoracion/<int:pk>/', ValoracionDetailView.as_view(), name='valoracion-detail'),
    path('valoracion/add/<int:pk>/', ValoracionCreateView.as_view(), name='valoracion-add'),
    path('valoracion/<int:pk>/update', ValoracionUpdateView.as_view(), name='valoracion-update'),
    path('valoracion/<int:pk>/delete', ValoracionDeleteView.as_view(), name='valoracion-delete'),

    #  urls para reserva
    path('reserva/', ReservaListView.as_view(), name='reserva-list' ),
    path('reserva/<int:pk>/', ReservaDetailView.as_view(), name='reserva-detail' ),
    path('reserva/add', ReservaCreateView.as_view(), name='reserva-add' ),
    path('reserva/<int:pk>/update', ResevaUpdateView.as_view(), name='reserva-update'),
    path('reserva/<int:pk>/delete', ReservaDeleteView.as_view(), name='reserva-delete'),

    #  urls para encargo
    path('encargo/add/<int:pk>', EncargoCreateView.as_view(), name='encargo-add'),
    path('encargo/<int:pk>/update', EncargoUpdateView.as_view(), name='encargo-update'),
    path('encargo/<int:pk>/delete', EncargoDeleteView.as_view(), name='encargo-delete'),

    #  urls para reserva pendiente
    path('reserva/pendientes', PendienteListView.as_view(), name='pendiente-list'),
    path('reserva/pendientes/<int:pk>/update', PendienteUpdateView.as_view(), name='pendiente-update'),

    #  urls para Ingredientes
    path('ingrediente', Ingredientelistview.as_view(), name='ingrediente-list'),
    path('ingrediente/<int:pk>', IngredienteDetailView.as_view(), name='ingrediente-detail'),
    path('ingrediente/add', IngredienteCreateView.as_view(), name='ingrediente-add'),
    path('ingrediente/<int:pk>/update', IngredienteUpdateView.as_view(), name='ingrediente-update'),
    path('ingrediente/<int:pk>/delete', IngredienteDeleteView.as_view(), name='ingrediente-delete'),

    #  urls para componenetes
    path('componente', ComponenteListView.as_view(), name='componente-list'),
    path('componente/<int:pk>', ComponenteDetailView.as_view(), name='componente-detail'),
    path('componente/add', ComponenteCreateView.as_view(), name='componente-add'),
    path('componente/<int:pk>/update', ComponenteUpdateview.as_view(), name='componente-update'),
    path('componente/<int:pk>/delete', ComponenteDeleteView.as_view(), name='componente-delete'),

    #   url para alejernos de producto
    path('aleproducto', AleProductoListeview.as_view(), name='aleproducto-list'),
    path('aleproducot/<int:pk>', AleProductoDetailview.as_view(), name='aleproducto-detail'),
    path('aleproducto/add', AleProductoCreateView.as_view(), name='aleproducto-add'),
    path('aleproducto/<int:pk>/update', AleProductoUpdateView.as_view(), name='aleproducto-update'),
    path('alepreducto/<int:pk>/delete', AleProductoDeleteView.as_view(), name='aleproducto-delete'),

    #  urls para django_registration
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),

    #path('accounts/login/', auth_views.LoginView.as_view(template_name='django_registration/login.html'), name='login'),
    #path('login/', LoginView.as_view(template_name='laguindaapi/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # FIDO2
    path('', include('django_fido.urls')),

    #  url para api
    #path('api/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # urls para busqueda
    path('search_producto/', Search_producto.as_view(), name='search_producto')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)