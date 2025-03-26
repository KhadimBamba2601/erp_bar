from django.db import models
from stock.models import Producto

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('enviado', 'Enviado'), ('entregado', 'Entregado')],
        default='pendiente'
    )

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"

    def calcular_total(self):
        total = sum(detalle.cantidad * detalle.precio_unitario for detalle in self.detallepedido_set.all())
        self.total = total
        self.save()

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    def save(self, *args, **kwargs):
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio
        super().save(*args, **kwargs)
        self.pedido.calcular_total()