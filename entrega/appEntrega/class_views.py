from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Cliente, Auto
from django.urls import reverse_lazy


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