# Django API Suite

Este proyecto es un backend desarrollado con Django que implementa una API REST escalable y estructurada.

## Objetivo

Construir una aplicación de backend robusta utilizando Django Framework, implementando patrones de diseño modernos y buenas prácticas para el desarrollo de APIs RESTful.

## Características

- ✅ Framework Django 5.2.4
- ✅ Django Rest Framework para APIs
- ✅ Integración con Firebase Realtime Database
- ✅ Renderizado del lado del servidor (SSR)
- ✅ Gestión de archivos estáticos
- ✅ Estructura modular con aplicaciones Django

## Aplicaciones

- **Homepage**: Página principal con plantillas y archivos estáticos
- **Landing API**: API REST para interacción con Firebase
- **Demo REST API**: Ejemplos y demostraciones de endpoints

## Instalación

1. Clonar el repositorio
2. Crear ambiente virtual: `python -m venv env`
3. Activar ambiente: `source env/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Ejecutar migraciones: `python manage.py migrate`
6. Iniciar servidor: `python manage.py runserver`

## Endpoints

- `/` - Información de la API
- `/homepage/index/` - Página principal
- `/landing/api/index/` - API REST Firebase
- `/admin/` - Panel de administración Django