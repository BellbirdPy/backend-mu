# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-30 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establecimiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_establecimiento_comprador', models.CharField(max_length=32)),
                ('nombre_comprador', models.CharField(max_length=100)),
                ('numero_guia', models.IntegerField()),
                ('fecha_venta', models.DateField()),
                ('tipo_venta', models.CharField(default='lote', max_length=10)),
                ('precio_total', models.BigIntegerField(blank=True, default=0, null=True)),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='establecimiento.Establecimiento')),
            ],
        ),
    ]
