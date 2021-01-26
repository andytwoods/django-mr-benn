=====
Usage
=====

To use django-mr-benn in a project, add it to your `INSTALLED_APPS`:

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
