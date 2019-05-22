from django.urls import path
from .views import *
from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', CrearAlumno.as_view(), name="crear_alumno"),
    path('listar_alumnos/', ListarAlumnos.as_view(), name="listar_alumnos"),

]