from django.urls import path
from .views import *
from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('crear_profesor', CrearProfesor.as_view(), name="crear_profesor"),
    path('listar_profesores/', ListarProfesors.as_view(), name="listar_profesors"),

]