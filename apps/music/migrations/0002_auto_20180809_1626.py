# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-09 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6, verbose_name='歌曲时长'),
        ),
    ]
