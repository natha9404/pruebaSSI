from django.urls import path
from .views import *
from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', CrearMateria.as_view(), name="crear_materia"),
    path('listar_materias/', ListarMaterias.as_view(), name="listar_materias"),
    path('ver_estudiantes/', VerEstudiantes.as_view(), name="ver_estudiantes"),

]