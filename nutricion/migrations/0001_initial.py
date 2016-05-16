# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establecimiento', '0002_auto_20160503_0234'),
        ('lote', '0002_auto_20160503_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutricion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('tipo_nutricion', models.TextField()),
                ('tipo_comida', models.TextField()),
                ('descripcion_comida', models.TextField(blank=True, null=True)),
                ('kilos', models.FloatField()),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutriciones', to='establecimiento.Establecimiento')),
                ('lotes', models.ManyToManyField(related_name='nutriciones', to='lote.Lote')),
            ],
        ),
    ]
