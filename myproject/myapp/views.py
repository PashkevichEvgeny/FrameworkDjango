from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Привет МИР!')


def about(request):
    return HttpResponse('About us')
