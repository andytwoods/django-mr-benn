import os

from debug_toolbar.utils import get_name_from_obj
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import re

from django.http import Http404
from django.template import loader
from django.urls import resolve


def render_mrbenn(request, response):
    t = loader.get_template('django_mr_benn/base.html')
    context = view_info(request)
    return t.render(context)


class MrBennMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        response = self.get_response(request)

        # adapted from https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/middleware.py
        content = response.content.decode(response.charset)
        insert_before = "</body>"
        pattern = re.escape(insert_before)
        bits = re.split(pattern, content, flags=re.IGNORECASE)
        if len(bits) > 1:
            bits[-2] += render_mrbenn(request, response)
            response.content = insert_before.join(bits)
            if "Content-Length" in response:
                response["Content-Length"] = len(response.content)
        return response

# adapted from https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/panels/request.py
def view_info(request):
    try:
        match = resolve(request.path)
        func, args, kwargs = match
        view = get_name_from_obj(func)

        if getattr(match, "url_name", False):
            url_name = match.url_name
            if match.namespaces:
                url_name = ":".join([*match.namespaces, url_name])
        else:
            url_name = _("<unavailable>")

        file_el = settings.BASE_DIR
        file_el = os.path.join(file_el, view.replace('.', os.sep))
        file_split = file_el.split(os.sep)
        file = os.sep.join(file_split[:-1]) + '.py'
        el = file_split[-1]
        return {'view': view, 'url_name': url_name, 'url': request.path, 'file': file, 'el': el}

    except Http404:
        pass
