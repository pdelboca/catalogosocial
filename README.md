# Catalogo Social

Catálogo de datos abiertos de la República Argentina que apunta a servir como backup ciudadano de los datos estatales.

https://catalogosocial.fly.dev/

Basado en [django-dcat](https://github.com/pdelboca/django-dcat) y [Sustainable CSS](https://github.com/pdelboca/sustainable-css/)

## Notas sobre el portal

Catálogo Social es un portal de datos abiertos simple y basado en DCAT. Actualmente se limita a listar catálogos y proveer un
enlace de descarga a los portales oficiales. Toda su información se importa desde data.json provistos por los Portales de
Datos Abiertos de la República Argentina. (Por ejemplo: https://datos.gob.ar/data.json o https://datos.yvera.gob.ar/data.json)

## Desarrollo local

1. Crear un entorno virtual:

    `pip -m venv .venv`

2. Instalar los requerimientos:

    `pip install -r requirements.txt -r dev-requirements.txt`

3. Correr migraciones

    `python manage.py migrate`

4. Ejecutar el servidor de desarrollo

    `python manage.py runserver`

## Notas sobre el desarrollo

A nivel técnico, el portal está hecho en Django, HTML y CSS. Busca ser sencillo, facil de desarrollar y desplegar. Sin
sobre ingeniería ni optimización prematura.

Está hecho con ❤️ y en los ratos libres.
