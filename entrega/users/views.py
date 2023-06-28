from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm

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
