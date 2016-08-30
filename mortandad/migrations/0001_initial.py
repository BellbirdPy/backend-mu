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
            name='Mortandad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('M', 'Mortandad'), ('A', 'Abigeo')], default='M', max_length=1)),
                ('fecha', models.DateTimeField()),
                ('razon', models.TextField()),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mortandades', to='establecimiento.Establecimiento')),
            ],
        ),
    ]
