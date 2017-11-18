# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-18 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20171115_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_at',
            field=models.TimeField(default='00:00', verbose_name='End at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_at',
            field=models.TimeField(default='00:00', verbose_name='Start at'),
            preserve_default=False,
        ),
    ]