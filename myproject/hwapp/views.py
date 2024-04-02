import logging

from django.http import HttpResponse
from django.shortcuts import render


logger = logging.getLogger(__name__)

# Create your views here.


def main(request):
    logger.debug('Main page accessed')
    return HttpResponse(html_main)


def about(request):
    logger.debug('About page accessed')
    return HttpResponse(html_about)


html_main = """<!DOCTYPE html>
<html>
    <head>
        <title>Главная</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <div>
            Это главная страница первого сайта сделанного на фреймворке Django.
        </div>
    </body>
</html>
"""

html_about = """<!DOCTYPE html>
<html>
    <head>
        <title>Обо мне</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <div>
            Страница об авторе этого сайта.
        </div>
        <div>
            Уже умею писать "Hello world" в трех Python фреймворках.
        </div>
    </body>
</html>
"""