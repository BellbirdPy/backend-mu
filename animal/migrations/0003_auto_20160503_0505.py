# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-03 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_auto_20160503_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='peso_especifico',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
