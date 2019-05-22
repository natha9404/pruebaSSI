from django.db import models
from profesores.models import Profesor


# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    profesor = models.ForeignKey('profesores.Profesor', on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre

