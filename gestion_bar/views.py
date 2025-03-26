from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.apps import apps

@login_required
def lista_productos(request):
    Producto = apps.get_model('ventas_online', 'Producto')
    productos = Producto.objects.all()
    return render(request, 'gestion_bar/lista_productos.html', {'productos': productos})

@login_required
def lista_pedidos(request):
    Pedido = apps.get_model('ventas_online', 'Pedido')
    pedidos = Pedido.objects.all()
    return render(request, 'gestion_bar/lista_pedidos.html', {'pedidos': pedidos})