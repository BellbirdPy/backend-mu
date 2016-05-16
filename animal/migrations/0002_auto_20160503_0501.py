# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-03 05:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuracion', '0001_initial'),
        ('lote', '0001_initial'),
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='lote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animales', to='lote.Lote'),
        ),
        migrations.AddField(
            model_name='animal',
            name='raza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animales', to='configuracion.Raza'),
        ),
    ]
