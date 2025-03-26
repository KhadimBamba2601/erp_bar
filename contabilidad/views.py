from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Transaccion

@login_required
@permission_required('contabilidad.view_transaccion', raise_exception=True)
def lista_transacciones(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'contabilidad/lista_transacciones.html', {'transacciones': transacciones})