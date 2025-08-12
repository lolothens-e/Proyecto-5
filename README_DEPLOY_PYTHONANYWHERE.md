# Despliegue en PythonAnywhere (Guía 22)

## Requisitos
- Cuenta en PythonAnywhere (Beginner)
- Clave privada Firebase Admin SDK: `secrets/landing-key.json`

## Pasos

1) Consola (Bash)
- Crear virtualenv Python 3.10:
  mkvirtualenv --python=/usr/bin/python3.10 env
- Clonar repo y entrar:
  git clone https://github.com/<USUARIO-GITHUB>/django_api_suite.git
  cd django_api_suite
- Instalar dependencias:
  pip install -r requirements.txt

2) Subir clave privada
- En Files -> abrir carpeta `django_api_suite`
- Crear carpeta `secrets` y subir `landing-key.json`

3) Ajustar settings.py
- Agregar su dominio en ALLOWED_HOSTS: `'<USUARIO>.pythonanywhere.com'`
- STATIC_ROOT ya configurado a `assets/`

4) Recolectar estáticos
- En una consola dentro del proyecto:
  python manage.py collectstatic
- Verifique carpeta `assets/` creada

5) Configurar WebApp (Manual configuration, Python 3.10)
- Virtualenv: `/home/<USUARIO>/.virtualenvs/env/`
- Static files: URL `/static/` -> `/home/<USUARIO>/django_api_suite/assets/`
- Working directory: `/home/<USUARIO>/django_api_suite`
- WSGI file: usar plantilla de abajo sustituyendo `<USUARIO>`

```
import os
import sys
project_home = '/home/<USUARIO>/django_api_suite'
if project_home not in sys.path:
    sys.path.insert(0, project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend_data_server.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

6) Reload
- En la sección Web, click en Reload y pruebe:
  http://<USUARIO>.pythonanywhere.com/

## Notas
- Asegúrese que `secrets/` está en `.gitignore` (ya lo está en este repo)
- Firebase Admin SDK se inicializa vía settings con `databaseURL` correcto
