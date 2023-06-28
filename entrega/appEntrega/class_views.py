from typing import Any
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Cliente, Auto, HistorialTrabajos
from django.urls import reverse_lazy


# Cliente

class ListaClientes(ListView):
    model = Cliente
    template_name = "appEntrega/classviews/lista_clientes.html"

    def get_queryset(self):
        return Cliente.objects.order_by('apellido')

class DetalleCliente(DetailView):
    model = Cliente
    template_name = "appEntrega/classviews/detalles_clientes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = self.object
        autos = Auto.objects.filter(cliente=cliente)
        context['cliente'] = cliente
        context['autos'] = autos
        return context

class BorrarCliente(DeleteView):
    model =  Cliente
    success_url = reverse_lazy("Clientes")
    template_name = "appEntrega/classviews/borrar_cliente.html"

class EditarCliente(UpdateView):
    model = Cliente
    success_url = reverse_lazy("Clientes")
    fields = ['nombre', 'apellido', 'telefono']
    template_name = "appEntrega/classviews/editar_cliente.html"



# Autos

class DetalleAuto(DetailView):
    model = Auto
    template_name = "appEntrega/classviews/detalles_autos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        autos = self.object
        historial = HistorialTrabajos.objects.filter(auto=autos)
        context['autos'] = autos
        context['historial'] = historial
        return context

class BorrarAuto(DeleteView):
    model = Auto
    success_url = reverse_lazy("Clientes")
    template_name = "appEntrega/classviews/borrar_auto.html"

class BorrarHistorial(DeleteView):
    model = HistorialTrabajos
    success_url = reverse_lazy("Clientes")
    template_name = "appEntrega/classviews/borrar_historial.html"

