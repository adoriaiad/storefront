# Prerequisites
1) Install latest version of Python from official web site

2) Install the development environment:

> pip3 install pipenv 

In VsCode -> extension -> search for Python intellisense extension

# Create a Django Project
Create a new project directory:
> mkdir storefront
> cd storefront

Create a virtual environment:
> pipenv install django

Launch subshell in virtual env
> pipenv shell
Now use django admin to start the new project:
> django-admin storefront .
> pipenv --venv
> python manage.py startapp playground

# Debugging
- Click on Run&Debug icon
- CLick on create a launch.json
- select Django and run the debug

# Django debug Toolbar
Installation on terminal:
> pipenv install django-debug-toolbar

Follow the instructions on the official web site to
- Add 'debug-toolbar' in INSTALLED_APPS (settings.py)
- Add the URLs in urls.py
- Add the Middleware in settings.py
- Add the Internal IPS
- Finally run the server and open the browser to 127.0.0.1:8000, the debug toolbar is available!