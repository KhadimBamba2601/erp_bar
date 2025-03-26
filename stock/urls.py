from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('editar-producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
]