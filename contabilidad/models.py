from django.db import models
from ventas_online.models import Pedido

class Transaccion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(
        max_length=10,
        choices=[('ingreso', 'Ingreso'), ('gasto', 'Gasto')]
    )

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"