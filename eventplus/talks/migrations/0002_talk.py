# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-29 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('start_at', models.TimeField(verbose_name='Start at')),
                ('end', models.TimeField(verbose_name='End')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('description_file', models.URLField(verbose_name='Explanatory File')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talks', to='talks.Speaker', verbose_name='Speaker')),
            ],
        ),
    ]
