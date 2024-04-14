from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
urls = {'sem3app/': ['main/',
                     'about/',
                     'head-tails/10',
                     'dice/10',
                     'rand100/10',
                     'author/1',
                     'post/1'],
        'sem4app/': ['form/',
                     'game/',
                     'add-author/',
                     'add-post/',
                     'post/1'],}


def index(request):
    return render(request, 'index.html', {'urls': urls})


def about(request):
    return HttpResponse('About us')
