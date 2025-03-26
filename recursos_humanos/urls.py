from django.urls import path
from . import views

app_name = 'recursos_humanos'
urlpatterns = [
    path('empleados/', views.lista_empleados, name='lista_empleados'),
]