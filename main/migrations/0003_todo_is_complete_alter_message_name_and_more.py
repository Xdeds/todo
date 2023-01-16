# Generated by Django 4.1.4 on 2023-01-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(verbose_name='Сообщение'),
        ),
    ]
