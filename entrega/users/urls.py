from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='Logout'),
    path('register/', views.register, name='Register'),
    path('edit-user/', views.edit_user, name='EditarUsuario'),
    path('perfil/', views.perfil, name='Perfil')

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)