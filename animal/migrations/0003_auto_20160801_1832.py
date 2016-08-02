# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-01 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_auto_20160721_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='estado',
            field=models.CharField(choices=[('V', 'Vivo'), ('M', 'Muerto'), ('E', 'Eliminado'), ('S', 'Vendido')], default='V', max_length=1),
        ),
    ]