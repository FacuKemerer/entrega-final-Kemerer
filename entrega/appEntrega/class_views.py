from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Cliente, Auto, HistorialTrabajos
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


# Cliente

class ListaClientes(AdminRequiredMixin, ListView):
    model = Cliente
    template_name = "appEntrega/classviews/lista_clientes.html"

    def get_queryset(self):
        return Cliente.objects.order_by('apellido')

class DetalleCliente(AdminRequiredMixin, DetailView):
    model = Cliente
    template_name = "appEntrega/classviews/detalles_clientes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = self.object
        autos = Auto.objects.filter(cliente=cliente)
        context['cliente'] = cliente
        context['autos'] = autos
        return context

class BorrarCliente(AdminRequiredMixin, DeleteView):
    model =  Cliente
    success_url = reverse_lazy("Clientes")
    template_name = "appEntrega/classviews/borrar_cliente.html"

class EditarCliente(AdminRequiredMixin, UpdateView):
    model = Cliente
    success_url = reverse_lazy("Clientes")
    fields = ['nombre', 'apellido', 'telefono']
    template_name = "appEntrega/classviews/editar_cliente.html"


# Autos

class DetalleAuto(AdminRequiredMixin, DetailView):
    model = Auto
    template_name = "appEntrega/classviews/detalles_autos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        autos = self.object
        historial = HistorialTrabajos.objects.filter(auto=autos)
        context['autos'] = autos
        context['historial'] = historial
        return context

class BorrarAuto(AdminRequiredMixin, DeleteView):
    model = Auto
    success_url = reverse_lazy("Clientes")
    template_name = "appEntrega/classviews/borrar_auto.html"

class BorrarHistorial(AdminRequiredMixin, DeleteView):
    model = HistorialTrabajos
    success_url = reverse_lazy("Clientes")
    template_name = "appEntrega/classviews/borrar_historial.html"

class EditarHistorial(AdminRequiredMixin, UpdateView):
    model = HistorialTrabajos
    success_url = reverse_lazy("Clientes")
    fields = ['descripcion']
    template_name = "appEntrega/classviews/editar_historial.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        historial = self.get_object()
        context['patente'] = historial.auto.patente
        return context