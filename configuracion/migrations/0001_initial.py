# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-05 06:27
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
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(default='', max_length=20)),
                ('nombre', models.CharField(max_length=80)),
                ('is_hembra', models.BooleanField()),
                ('establecimiento', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='establecimiento.Establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Pajuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.TextField(blank=True, default='')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pajuelas', to='establecimiento.Establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.TextField(blank=True, default='')),
                ('establecimiento', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='razas', to='establecimiento.Establecimiento')),
            ],
        ),
    ]
