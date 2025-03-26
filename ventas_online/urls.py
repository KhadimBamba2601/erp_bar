from django.urls import path
from . import views

app_name = 'ventas_online'
urlpatterns = [
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('catalogo/', views.catalogo_productos, name='catalogo_productos'),
    path('realizar-pedido/', views.realizar_pedido, name='realizar_pedido'),
    path('actualizar-pedido/<int:pedido_id>/', views.actualizar_pedido, name='actualizar_pedido'),
]