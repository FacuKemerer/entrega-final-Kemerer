"""
URL configuration for projecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from appEntrega import views
from appEntrega import class_views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('horarios/', views.horarios, name="Horarios"),
    path('trabajos/', views.trabajos, name="Trabajos"),
    path('form-hist/', views.agregar_historia, name="AgregarHistorial"),
    path('form-cliente/', views.agregar_cliente, name="AgregarCliente"),
    path('form-auto/', views.agregar_auto, name="AgregarAuto"),
    path('busqueda/', views.busqueda_auto, name="Busqueda"),
    # path('registrarse/', views.sign_up, name="Registrarse"),
    # path('cerrar-sesion', views.sign_out, name="CerrarSesion"),
    # path('', views., name=""),
]

urlpatterns += [
    path('clientes/', class_views.ListaClientes.as_view(), name="Clientes"),
    path('detalles/<pk>', class_views.DetalleCliente.as_view(), name="Detalles"),
    path('borrar-cliente/<pk>', class_views.BorrarCliente.as_view(), name="Borrar"),
    path('editar/<pk>', class_views.EditarCliente.as_view() , name="Editar"),
    path('detalles-autos/<pk>', class_views.DetalleAuto.as_view() , name="DetalleAuto"),
    path('borrar-auto/<pk>', class_views.BorrarAuto.as_view() , name="BorrarAuto"),
    path('borrar-historial/<pk>', class_views.BorrarHistorial.as_view() , name="BorrarHistorial"),
    # path('', class_views. , name=""),
]