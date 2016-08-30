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
            name='Egreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(default='', max_length=80)),
                ('rubro', models.CharField(choices=[('GD', 'Gastos Directos'), ('GA', 'Gastos Administrativos'), ('IT', 'Impuestos y Tazas'), ('GC', 'Gastos de Comercializaci\xf3n'), ('GF', 'Gastos Financieros')], default='GD', max_length=2)),
                ('monto', models.PositiveIntegerField()),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='egreso', to='establecimiento.Establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='IngresoVario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('motivo', models.CharField(default='', max_length=80)),
                ('comprador', models.CharField(default='', max_length=80)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.PositiveIntegerField()),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingreso_vario', to='establecimiento.Establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='IngresoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('comprador', models.CharField(default='', max_length=80)),
                ('cantidad', models.PositiveIntegerField()),
                ('categoria', models.CharField(max_length=80)),
                ('carimbo', models.PositiveIntegerField()),
                ('peso_promedio', models.FloatField(blank=True, null=True)),
                ('total', models.PositiveIntegerField()),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingreso_venta', to='establecimiento.Establecimiento')),
            ],
        ),
    ]
