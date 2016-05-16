# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mortandad', '0001_initial'),
        ('animal', '0006_remove_animal_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='mortandad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animales', to='mortandad.Mortandad'),
        ),
    ]
