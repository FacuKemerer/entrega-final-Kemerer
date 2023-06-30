from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegisterForm, EditarUser, PostForm
from .models import Avatar, Post
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
        form = EditarUser(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            try:
                avatar = Avatar.objects.get(user=usuario)
                avatar_file_name = avatar.avatar.name  # Guardar el nombre de archivo del avatar anterior
            except Avatar.DoesNotExist:
                avatar = Avatar(user=usuario)
                avatar_file_name = None
            avatar_file = request.FILES.get('avatar')
            if avatar_file:
                avatar.avatar = avatar_file
                if avatar_file_name and avatar_file_name != avatar.avatar.name:
                    avatar.avatar.storage.delete(avatar_file_name)
            avatar.save()
            return render(request, "appEntrega/index.html")
    else:
        form = EditarUser(initial={'email': usuario.email, 'last_name': usuario.last_name, 'first_name': usuario.first_name})
    return render(request, "users/editar_perfil.html", {"form": form, "usuario": usuario})

@login_required
def perfil(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    default_url = r'/media/avatares/Avatar.png'
    url = default_url
    if avatares:
        url = avatares[0].avatar.url
    return render(request, "users/perfil.html", {"url": url})

def mostrar_imagen_post(post):
    url = post.image.url if post.image else None
    return url

def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.title = form.cleaned_data['title']
            post.image = form.cleaned_data['image']
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('Trabajos')
    else:
        form = PostForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'users/publicar.html', context)



def trabajos(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'users/Trabajos.html', context)