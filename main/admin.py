from django.contrib import admin
from main.models import Message, Todo
admin.site.register(Todo)
admin.site.register(Message)