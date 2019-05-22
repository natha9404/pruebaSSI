from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(max_length=12)

    def __str__(self):
        return self.nombre