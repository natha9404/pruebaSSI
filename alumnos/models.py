from django.db import models
from materias.models import Materia

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    DNI = models.CharField(max_length=10)
    PIN = models.CharField(max_length=10)
    materia = models.ManyToManyField(Materia)

    def __str__(self):
        return self.nombre