from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Empleado

@login_required
@permission_required('recursos_humanos.view_empleado', raise_exception=True)
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'recursos_humanos/lista_empleados.html', {'empleados': empleados})