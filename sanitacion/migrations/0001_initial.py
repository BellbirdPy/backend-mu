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
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('color', models.CharField(default='', max_length=7)),
                ('allDay', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventoEstablecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('color', models.CharField(default='#CDDC39', max_length=7)),
                ('veterinario', models.TextField()),
                ('allDay', models.BooleanField(default=True)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='establecimiento.Establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vacunacion', models.DateField()),
                ('nombre', models.CharField(default='', max_length=50)),
                ('nombre_cientifico', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('veterinario', models.CharField(default='', max_length=40)),
                ('enfermedad', models.CharField(default='', max_length=30)),
                ('codigo', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacunaciones', to='establecimiento.Establecimiento')),
            ],
        ),
    ]
