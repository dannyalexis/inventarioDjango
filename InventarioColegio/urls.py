"""InventarioColegio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view =  get_schema_view(
    openapi.Info(
        title = "Api de gestion de inventario",
        default_version="v1",
        description="api usando rest_framewok  para el manejo de inventario ",
        terms_of_services = "www.google.com",
        contac = openapi.Contact(email="alex15_25@hotmail.com"),
        license=openapi.License(name="MIT")
    ),
    public=True,
    permission_classes = (permissions.AllowAny, ),

)


urlpatterns = [
    path('',schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc', schema_view.with_ui('redoc',cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('administracion/', include('administracion.urls')),
]
