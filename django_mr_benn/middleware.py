from django.conf import settings
import re

from django.template import loader


def render_mrbenn():
    t = loader.get_template('django_mr_benn/base.html')
    return t.render({})


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
            bits[-2] += render_mrbenn()
            response.content = insert_before.join(bits)
            if "Content-Length" in response:
                response["Content-Length"] = len(response.content)
        return response
