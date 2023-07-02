from .forms import CambiarPasswordForm
from .models import Post
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class BorrarPerfil(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("Inicio")
    template_name = "users/borrar_perfil.html"

class CambiarPasswordView(LoginRequiredMixin, View):
    template_name = "users/editar_contraseña.html"
    form_class = CambiarPasswordForm
    success_url = reverse_lazy("Inicio")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})
    
    def post(self, request, *args, **kwargs):
        
        usuario = User.objects.get(id=request.user.id)
        form = self.form_class(request.POST)
        
        if form.is_valid():
            pass1 = form.cleaned_data.get("password1")
            pass2 = form.cleaned_data.get("password2")
        
            if pass1 == pass2:
                usuario.set_password(pass1)
                usuario.save()
                return render(request, "appEntrega/index.html")

class BorrarPost(DeleteView):
    model =  Post
    success_url = reverse_lazy("Trabajos")
    template_name = "users/borrar_post.html"