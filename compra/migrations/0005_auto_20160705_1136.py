# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 15:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0004_auto_20160524_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='fecha',
            new_name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateField(default=datetime.datetime(2016, 7, 5, 15, 36, 32, 917072, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='numero_guia',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
