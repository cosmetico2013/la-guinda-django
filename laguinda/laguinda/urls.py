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
from laguindaapi.views import ProductoListView, ProductoDetailView, ProductoCreateView, ProductoDeleteView, ProductoUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('producto/', ProductoListView.as_view(), name='producto-list' ),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('producto/add/', ProductoCreateView.as_view(), name='producto-add'),
    path('producto/<int:pk>/update/', ProductoUpdateView.as_view(), name='producto-update'),
    path('producto/<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto-delete'),

    path('accounts/', include('django.contrib.auth.urls')),
]
