# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-01 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortandad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mortandad',
            name='fecha',
            field=models.DateField(),
        ),
    ]
