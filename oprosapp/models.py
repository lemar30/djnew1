from django.db import models

# Create your models here.
class People (models.Model):
    name = models.CharField (max_length=20, verbose_name='Имя')
    tel = models.IntegerField (verbose_name='Телефон')

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'