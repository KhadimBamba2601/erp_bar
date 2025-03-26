from django.urls import path
from . import views

app_name = 'contabilidad'
urlpatterns = [
    path('transacciones/', views.lista_transacciones, name='lista_transacciones'),
]