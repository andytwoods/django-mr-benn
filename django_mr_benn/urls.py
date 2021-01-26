# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'django_mr_benn'
urlpatterns = [
    url(r'mrbenn/', views.action, name='gitabix-action'),
]
