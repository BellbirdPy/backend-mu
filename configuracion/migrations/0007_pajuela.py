# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-15 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0007_auto_20160519_2134'),
        ('configuracion', '0006_auto_20160705_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pajuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.TextField(blank=True, default='')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pajuelas', to='establecimiento.Establecimiento')),
            ],
        ),
    ]
