from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Producto, Categoria
from django import forms
from django.contrib import messages

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'stock', 'descripcion', 'disponible']

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'stock/lista_productos.html', {'productos': productos})

@login_required
@permission_required('stock.add_producto', raise_exception=True)
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto agregado con éxito")
            return redirect('stock:lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'stock/agregar_producto.html', {'form': form})

@login_required
@permission_required('stock.change_producto', raise_exception=True)
def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f"Producto {producto.nombre} actualizado")
            return redirect('stock:lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'stock/editar_producto.html', {'form': form, 'producto': producto})