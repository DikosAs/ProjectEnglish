from django.urls import path
from .views import *

urlpatterns = [
    path('', re_en),
    path('ru/', ru_index, name='ru_index'),
    path('en/', en_index, name='en_index'),
    path('.well-known/pki-validation/7014A47370A46826C34B32728BCC3723.txt', ssl_auth)
]