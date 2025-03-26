from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from stock.models import Producto
from ventas_online.models import Pedido, DetallePedido
from contabilidad.models import Transaccion
from logistica.models import Envio
from django.db import models

@login_required
def inicio(request):
    productos_total = Producto.objects.count()
    stock_bajo = Producto.objects.filter(stock__lt=10).count()
    pedidos_pendientes = Pedido.objects.filter(estado='pendiente').count()
    ingresos_total = Transaccion.objects.filter(tipo='ingreso').aggregate(total=models.Sum('monto'))['total'] or 0
    envios_en_transito = Envio.objects.filter(estado='en_transito').count()

    context = {
        'productos_total': productos_total,
        'stock_bajo': stock_bajo,
        'pedidos_pendientes': pedidos_pendientes,
        'ingresos_total': ingresos_total,
        'envios_en_transito': envios_en_transito,
    }
    return render(request, 'inicio.html', context)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'usuario/registro.html', {'form': form})

@login_required
def reportes(request):
    # Ventas por estado
    ventas_por_estado = Pedido.objects.values('estado').annotate(
        total=models.Sum('total'),
        cantidad=models.Count('id')
    )
    # Productos más vendidos
    productos_vendidos = DetallePedido.objects.values('producto__nombre').annotate(
        total_vendido=models.Sum('cantidad')
    ).order_by('-total_vendido')[:5]
    # Ingresos por mes
    ingresos_por_mes = Transaccion.objects.filter(tipo='ingreso').annotate(
        mes=models.functions.TruncMonth('fecha')
    ).values('mes').annotate(total=models.Sum('monto')).order_by('mes')

    context = {
        'ventas_por_estado': ventas_por_estado,
        'productos_vendidos': productos_vendidos,
        'ingresos_por_mes': ingresos_por_mes,
    }
    return render(request, 'reportes.html', context)