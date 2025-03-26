from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre