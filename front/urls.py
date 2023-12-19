from django.urls import path
from .views import *

urlpatterns = [
    path('', re_en),
    path('ru/', ru_index, name='ru_index'),
    path('en/', en_index, name='en_index'),
]