# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sigudong',
            fields=[
                ('cnum', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('si', models.CharField(max_length=15, verbose_name='si')),
                ('gu', models.CharField(blank=True, max_length=15, null=True, verbose_name='gu')),
                ('dong', models.CharField(blank=True, max_length=15, null=True, verbose_name='dong')),
            ],
        ),
    ]
