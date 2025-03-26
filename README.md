# Sistema ERP para Bar

## Descripción
Este es un sistema ERP (Enterprise Resource Planning) desarrollado específicamente para la gestión de un bar. El sistema integra múltiples módulos para manejar diferentes aspectos del negocio, desde la gestión de inventario hasta la contabilidad.

## Características Principales
- Gestión de inventario y stock
- Sistema de ventas online
- Gestión de recursos humanos
- Contabilidad
- Logística
- Gestión de bar

## Requisitos del Sistema
- Python 3.x
- Django 4.x
- SQLite3 (incluido por defecto)

## Instalación

1. Clonar el repositorio:
```bash
git clone [git@github.com:KhadimBamba2601/erp_bar.git]
cd erp_bar
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Realizar las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crear un superusuario:
```bash
python manage.py createsuperuser
```

6. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

## Estructura del Proyecto
```
erp_bar/
├── erp_bar/              # Configuración principal del proyecto
├── gestion_bar/          # Módulo de gestión del bar
├── ventas_online/        # Sistema de ventas online
├── stock/               # Gestión de inventario
├── recursos_humanos/    # Gestión de RRHH
├── contabilidad/        # Módulo contable
├── logistica/          # Gestión logística
├── static/             # Archivos estáticos
├── templates/          # Plantillas HTML
└── manage.py          # Script de gestión de Django
```

## Módulos Principales

### Gestión de Bar
- Gestión de productos
- Control de pedidos
- Gestión de mesas y reservas

### Ventas Online
- Catálogo de productos
- Sistema de pedidos
- Gestión de clientes

### Stock
- Control de inventario
- Gestión de proveedores
- Alertas de stock bajo

### Recursos Humanos
- Gestión de empleados
- Control de horarios
- Nóminas

### Contabilidad
- Facturación
- Control de gastos
- Reportes financieros

### Logística
- Gestión de proveedores
- Control de entregas
- Planificación de pedidos

## Uso del Sistema

1. Acceder al sistema:
   - URL: http://localhost:8000
   - Usar las credenciales de superusuario creadas

2. Navegación:
   - Panel principal: http://localhost:8000/
   - Administración: http://localhost:8000/admin/
   - Gestión de Bar: http://localhost:8000/gestion/
   - Ventas Online: http://localhost:8000/ventas/
   - Stock: http://localhost:8000/stock/
   - RRHH: http://localhost:8000/rrhh/
   - Contabilidad: http://localhost:8000/contabilidad/
   - Logística: http://localhost:8000/logistica/

## Seguridad
- Sistema de autenticación integrado
- Control de acceso basado en roles
- Protección contra CSRF
- Encriptación de contraseñas

## Mantenimiento
- Realizar copias de seguridad regulares de la base de datos
- Mantener actualizadas las dependencias
- Monitorear los logs del sistema

## Soporte
Para reportar problemas o solicitar ayuda:
1. Crear un issue en el repositorio
2. Describir detalladamente el problema
3. Incluir capturas de pantalla si es necesario

## Licencia
[Especificar la licencia del proyecto]

## Contribuciones
Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Crear una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Crear un Pull Request

## Contacto
[Información de contacto del mantenedor del proyecto] 
