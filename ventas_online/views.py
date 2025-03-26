from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Pedido, Cliente, DetallePedido
from stock.models import Producto
from contabilidad.models import Transaccion
from django import forms
from django.contrib import messages

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado']

@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'ventas_online/lista_pedidos.html', {'pedidos': pedidos})

@login_required
@permission_required('ventas_online.change_pedido', raise_exception=True)
def actualizar_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            messages.success(request, f"Estado del pedido {pedido.id} actualizado")
            return redirect('ventas_online:lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'ventas_online/actualizar_pedido.html', {'form': form, 'pedido': pedido})

def catalogo_productos(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'ventas_online/catalogo_productos.html', {'productos': productos})

def realizar_pedido(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        productos_ids = request.POST.getlist('productos')
        cantidades = request.POST.getlist('cantidades')

        # Validaciones básicas
        if not nombre or not email or not direccion:
            messages.error(request, "Por favor, completa todos los campos obligatorios.")
            return redirect('ventas_online:realizar_pedido')
        if not productos_ids or not any(int(c) > 0 for c in cantidades if c):
            messages.error(request, "Selecciona al menos un producto con cantidad mayor a 0.")
            return redirect('ventas_online:realizar_pedido')

        cliente, _ = Cliente.objects.get_or_create(
            email=email,
            defaults={'nombre': nombre, 'telefono': telefono, 'direccion': direccion}
        )

        pedido = Pedido.objects.create(cliente=cliente)

        for prod_id, cantidad in zip(productos_ids, cantidades):
            if cantidad and int(cantidad) > 0:
                producto = Producto.objects.get(id=prod_id)
                if producto.stock >= int(cantidad):
                    DetallePedido.objects.create(
                        pedido=pedido,
                        producto=producto,
                        cantidad=int(cantidad),
                        precio_unitario=producto.precio
                    )
                    producto.stock -= int(cantidad)
                    producto.save()
                else:
                    messages.error(request, f"No hay suficiente stock para {producto.nombre}")
                    pedido.delete()
                    return redirect('ventas_online:catalogo_productos')

        Transaccion.objects.create(
            pedido=pedido,
            descripcion=f"Venta online - Pedido {pedido.id}",
            monto=pedido.total,
            tipo='ingreso'
        )

        messages.success(request, "Pedido realizado con éxito")
        return redirect('ventas_online:catalogo_productos')
    
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'ventas_online/realizar_pedido.html', {'productos': productos})