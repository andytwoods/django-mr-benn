import webbrowser
from django.http import JsonResponse


def action(request):
    url = 'pycharm://open?file=/Users/andytwoods/django-gitabix/django_gitabix/apps.py'
    webbrowser.open(url, new=0, autoraise=True)
    return JsonResponse({})
