# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-13 04:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_auto_20170113_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contratista',
            name='actualidad',
        ),
        migrations.RemoveField(
            model_name='contratista',
            name='salida_empresa',
        ),
    ]