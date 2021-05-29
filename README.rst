================
Todo application
================

Make virtualenv
===============

On Linux::

   $ python3.6 -m venv venv
   $ . venv/bin/activate

On Windows::

   > python -m venv venv
   > venv/Scripts/activate

::

   (venv)$ pip install -r requirements.txt

migrate
=======

::

   (venv)$ python manage.py migrate

Make admin user
===============

::

   (venv)$ python manage.py createsuperuser

runserver
=========

::

   (venv)$ python manage.py runserver
