from django.contrib import admin
from .models import *


# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = [
        'en_tv_text',
        'ru_tv_text',
        'tv_statistic',
        'newspaper_statistic',
        'radio_statistic',
        'internet_statistic',
        'friend_statistic',
    ]


admin.site.register(Data, DataAdmin)
