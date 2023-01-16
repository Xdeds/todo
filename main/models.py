from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=225, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Создано в: ')
    is_complete = models.BooleanField(default=False)

class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    text = models.TextField(verbose_name='Сообщение')