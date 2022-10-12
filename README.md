# DjangoCRUDEmployeeExample


This is a basic example of CRUD(Create, Retrieve, Update and Delete) with Django Rest Framework.

Pre-requisites:
Python, Django

Steps to run the project:
1. Clone/ Download the project
2. Navigate inside the project folder and run "python manage.py makmigrations"
3. Run "python manage.py migrate"
4. Run python manage.py runserver

Now, your project must be up and runnning.
Please navigate to http://127.0.0.1:8000/api/ to see all the url endpoints.

Providing them up here as well for simplicity:

{
    "all": "http://127.0.0.1:8000/api/all",
    "add": "http://127.0.0.1:8000/api/create",
    "update": "http://127.0.0.1:8000/api/update/pk",
    "delete": "http://127.0.0.1:8000/api/delete/pk"
}

