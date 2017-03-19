# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-19 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photoalbumtree_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoalbumtree',
            name='date_published',
            field=models.DateTimeField(null=True, verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='photoalbumtree',
            name='published',
            field=models.BooleanField(default=False, verbose_name='опубликован'),
        ),
    ]