# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django_mr_benn import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', views.home, name='home'),
    url(r'^', include('django_mr_benn.urls', namespace='django_mr_benn')),
]
