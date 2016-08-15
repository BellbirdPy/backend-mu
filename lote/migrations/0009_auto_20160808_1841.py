# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-08 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_servicio_establecimiento'),
        ('sanitacion', '0008_vacunacion'),
        ('lote', '0008_auto_20160801_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='vacunacion',
            field=models.ManyToManyField(blank=True, default=None, related_name='lotes', to='sanitacion.Vacunacion'),
        ),
        migrations.RemoveField(
            model_name='lote',
            name='servicio',
        ),
        migrations.AddField(
            model_name='lote',
            name='servicio',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lotes', to='servicio.Servicio'),
        ),
    ]
