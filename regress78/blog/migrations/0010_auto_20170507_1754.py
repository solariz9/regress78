# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-07 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170507_1735'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='adv',
            managers=[
                ('list_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='adv',
            name='date_published',
            field=models.DateTimeField(default=None, null=True, verbose_name='дата публикации'),
        ),
        migrations.AddField(
            model_name='adv',
            name='published',
            field=models.BooleanField(default=False, verbose_name='опубликован'),
        ),
    ]
