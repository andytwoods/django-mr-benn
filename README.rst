=============================
django-mr-benn
=============================

.. image:: https://badge.fury.io/py/django-mr-benn.svg
    :target: https://badge.fury.io/py/django-mr-benn

.. image:: https://travis-ci.org/andytwoods/django-mr-benn.svg?branch=master
    :target: https://travis-ci.org/andytwoods/django-mr-benn

.. image:: https://codecov.io/gh/andytwoods/django-mr-benn/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/andytwoods/django-mr-benn

opehquickly open pytohn files from your frontend

Documentation
-------------

The full documentation is at https://django-mr-benn.readthedocs.io.

Quickstart
----------

Install django-mr-benn::

    pip install django-mr-benn

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_mr_benn.apps.DjangoMrBennConfig',
        ...
    )

Add django-mr-benn's URL patterns:

.. code-block:: python

    from django_mr_benn import urls as django_mr_benn_urls


    urlpatterns = [
        ...
        url(r'^', include(django_mr_benn_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
