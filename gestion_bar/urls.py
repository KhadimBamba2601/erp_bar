from django.urls import path
from . import views

app_name = 'gestion_bar'
urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
]