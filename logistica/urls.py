from django.urls import path
from . import views

app_name = 'logistica'
urlpatterns = [
    path('envios/', views.lista_envios, name='lista_envios'),
]