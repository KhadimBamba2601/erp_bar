from django.db import models
from ventas_online.models import Pedido

class Envio(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    transportista = models.CharField(max_length=100)
    fecha_envio = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=[('preparando', 'Preparando'), ('en_transito', 'En Tránsito'), ('entregado', 'Entregado')]
    )
    numero_seguimiento = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Envío de Pedido {self.pedido.id}"