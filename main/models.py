from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class Publication(models.Model):
    title = models.CharField(max_length=1000, unique=True, verbose_name='Заголовок')
    date = models.DateTimeField(default=datetime.now)
    shortDescription = models.CharField(max_length=10000, verbose_name='Короткое описание')
    content = models.TextField(verbose_name='Контент')
    clickCount = models.IntegerField(verbose_name='Количество переходов', default=0)
    likes = models.IntegerField(verbose_name='Количество лайков', default=0)
    def __str__(self):
        return self.title

class User(AbstractUser):
    ...