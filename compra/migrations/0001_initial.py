# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_establecimiento_vendedor', models.CharField(max_length=32)),
                ('nombre_vendedor', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carimbo', models.PositiveIntegerField()),
                ('cantidad', models.PositiveIntegerField()),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='configuracion.Categoria')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_compra', to='compra.Compra')),
                ('raza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='configuracion.Raza')),
            ],
        ),
    ]
