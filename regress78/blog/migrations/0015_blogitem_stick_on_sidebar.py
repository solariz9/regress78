# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-09 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170509_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogitem',
            name='stick_on_sidebar',
            field=models.BooleanField(default=False, verbose_name='закреплен в сайдбаре'),
        ),
    ]