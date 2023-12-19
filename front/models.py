from django.db import models


# Create your models here.
class Data(models.Model):
    en_tv_text = models.TextField('Отношение к телику EN', null=True, blank=True)
    ru_tv_text = models.TextField('Отношение к телику RU', null=True, blank=True)

    en_statistic_text = models.TextField('О статистике EN', null=True, blank=True)
    ru_statistic_text = models.TextField('О статистике RU', null=True, blank=True)

    tv_statistic = models.SmallIntegerField('Процент ТВ', null=True, blank=True)
    newspaper_statistic = models.SmallIntegerField('Процент ГАЗЕТ', null=True, blank=True)
    radio_statistic = models.SmallIntegerField('Процент РАДИО', null=True, blank=True)
    internet_statistic = models.SmallIntegerField('Процент ИНТЕРНЕТА', null=True, blank=True)
    friend_statistic = models.SmallIntegerField('Процент СЛУХОВ', null=True, blank=True)

    class Meta:
        verbose_name = "информацию"
        verbose_name_plural = "Информация"
