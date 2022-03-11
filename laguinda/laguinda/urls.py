"""laguinda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from laguindaapi import views
from laguindaapi.views import ProductoListView, ProductoDetailView, ProductoCreateView, ProductoDeleteView, ProductoUpdateView
from laguindaapi.views import ComentarioListView, ComentarioCreateView, ComentarioDeleteView, ComentarioUpdateView, ComentarioDetailView
from laguindaapi.views import ValoracionUpdateView, ValoracionDetailView, ValoracionCreateView, ValoracionDeleteView, ValoracionListView
from laguindaapi.views import Search_producto
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.models import User
from rest_framework import routers, viewsets, serializers

# contenido que proporciona la busqueda
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# vista para la api.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# url configuracion
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    #  urls para el index
    #path('', views.index, name='index.html'),

    #  urls para productos
    path('', ProductoListView.as_view(), name='producto-list' ),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('producto/add/', ProductoCreateView.as_view(), name='producto-add'),
    path('producto/<int:pk>/update/', ProductoUpdateView.as_view(), name='producto-update'),
    path('producto/<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto-delete'),

    #  urls para comentarios
    #path('comentario/', ComentarioListView.as_view(), name='comentario-list'),
    path('comentario/<int:pk>/', ComentarioDetailView.as_view(), name='comentario-detail'),
    path('comentario/add/<int:pk>/', ComentarioCreateView.as_view(), name='comentario-add'),
    path('comentario/<int:pk>/update/', ComentarioUpdateView.as_view(), name='comentario-update'),
    path('comentario/<int:pk>/delete/', ComentarioDeleteView.as_view(), name='comentario-delete'),

    #  urls para valoraciones
    #path('valoracion/', ValoracionListView.as_view(), name='valoracion-list'),
    path('valoracion/<int:pk>/', ValoracionDetailView.as_view(), name='valoracion-detail'),
    path('valoracion/add/<int:pk>/', ValoracionCreateView.as_view(), name='valoracion-add'),
    path('valoracion/<int:pk>/update', ValoracionUpdateView.as_view(), name='valoracion-update'),
    path('valoracion/<int:pk>/delete', ValoracionDeleteView.as_view(), name='valoracion-delete'),

    #  urls para django_registration
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    #path('accounts/login/', auth_views.LoginView.as_view(template_name='django_registration/login.html'), name='login'),
    #path('login/', LoginView.as_view(template_name='laguindaapi/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    #  url para api
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

    # urls para busqueda
    path('search_producto/', Search_producto.as_view(), name='search_producto')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)