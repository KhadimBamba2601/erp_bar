from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('reportes/', views.reportes, name='reportes'),
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion_bar.urls')),
    path('contabilidad/', include('contabilidad.urls')),
    path('rrhh/', include('recursos_humanos.urls')),
    path('logistica/', include('logistica.urls')),
    path('ventas/', include('ventas_online.urls')),
    path('stock/', include('stock.urls')),
]