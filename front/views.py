from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *


def get_data(request: WSGIRequest = None) -> Data or None:
    data = Data.objects.all()
    try:
        return data[0]
    except IndexError:
        return None


# Create your views here.
def re_en(request: WSGIRequest):
    return redirect(reverse('en_index'))


def ru_index(request: WSGIRequest):
    return render(request, 'ru/index.html', {'content': get_data()})


def en_index(request: WSGIRequest):
    return render(request, 'en/index.html', {'content': get_data()})


def ssl_auth(request: WSGIRequest):
    return render(request, 'ssl/7014A47370A46826C34B32728BCC3723.txt')
