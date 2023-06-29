from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from .models import Avatar

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "appEntrega/index.html", {"correcto":f"¡Bienvenido {usuario}!"})
        else:
                return render(request, "appEntrega/index.html", {"incorrecto": "Los datos que ingreso son incorrectos", "form": form})
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def register(request):
    if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                form.save()
                return render(request,"appEntrega/index.html" ,  {"mensaje":"¡El usuario se creo con exito!"})
    else:       
            form = UserRegisterForm()     
    return render(request,"users/register.html",  {"form":form})


@login_required
def edit_user(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "appEntrega/forms/confirmacion.html")
    else:
        form = UserEditForm(initial={'email': usuario.email})
    return render(request, "users/editar_perfil.html", {"form": form, "usuario": usuario})

@login_required
def perfil(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    default_url = r'/media/avatares/Avatar.png'
    url = default_url
    if avatares:
        url = avatares[0].avatar.url

    return render(request, "users/perfil.html", {"url": url})
