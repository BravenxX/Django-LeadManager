# LEAD MANAGER - BACKEND - DJANGO

José N.

## Herramientas

- Django

## Iniciar

1. En leadmanager

```
python manage.py runserver
```

2. Iniciar LeadManager_frontend:

https://github.com/BravenxX/React-LeadManager

## Tutorial

1. Para crear "enviroments", por consola:

```
pip3 install pipenv
```

2. Para crear ambiente virtual, En carpeta proyecto:

```
pipenv shell
```

3. Para instalar librerias:

```
pipenv install django
```

4. Crear django app:

```
django-admin startproject leadmanager
```

5. Seleccionar interpretador de python,

en vscode:

- control + shift + P
- Python select interpreter

Seleccionar el que esta en la carpeta leadmanager

6. Creamos otro django app, con el nombre leads

```
python manage.py startapp leads
```

7. En root/leadmanager/leadmanager/settings.py

agregar

```
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 +++   'leads',
 +++   'rest_framework'
]
```

8. Modelos se crean en leads/models.py

9. Creamos migration

```
python manage.py makemigrations leads
```

10. Para correr todas las migraciones

```
python manage.py migrate
```

11. Creamos serializers.py en leads

12. Creamos api.py en leads

13. Creamos las rutas en leadmanager/urls.py

14. Para iniciar el servidor python

en leadmanager

```
python manage.py runserver
```
