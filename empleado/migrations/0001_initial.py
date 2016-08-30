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
            name='Contratista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('numero_cedula', models.CharField(blank=True, max_length=12, null=True)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('actividad', models.CharField(max_length=40)),
                ('jornal', models.IntegerField()),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratistas', to='establecimiento.Establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('numero_cedula', models.CharField(max_length=12)),
                ('fecha_nacimiento', models.DateTimeField(null=True)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('ingreso_empresa', models.DateTimeField(null=True)),
                ('cargo', models.CharField(max_length=40)),
                ('salario', models.IntegerField()),
                ('ciudad_nacimiento', models.CharField(blank=True, max_length=30, null=True)),
                ('contacto_emergencia', models.TextField(blank=True, null=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('escaneo_cedula', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='establecimiento.Establecimiento')),
            ],
        ),
    ]
