from django.urls import path
from .views import *
from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('iniciar_sesion/', auth_views.LoginView.as_view(template_name='./iniciar_sesion.html'), name="iniciar_sesion"),
    path('salir/', auth_views.LogoutView.as_view(), {'next_page': 'iniciar_sesion'}, name="cerrar_sesion"),
    path('index/', ListarUsuarios.as_view(), name="index"),
    path('', auth_views.LoginView.as_view(template_name='./iniciar_sesion.html'), name="iniciar_sesion"),
    path('crear_usuario/', CrearUsuario.as_view(), name="crear_usuario"),
    path('editar_usuario/<int:pk>/', EditarUsuario.as_view(), name="editar_usuario"),
    path('listar_usuarios/', ListarUsuarios.as_view(), name="listar_usuarios"),

]