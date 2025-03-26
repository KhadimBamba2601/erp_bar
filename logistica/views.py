from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Envio

@login_required
@permission_required('logistica.view_envio', raise_exception=True)
def lista_envios(request):
    envios = Envio.objects.all()
    return render(request, 'logistica/lista_envios.html', {'envios': envios})