# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-21 01:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inseminacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleinseminacion',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 10, 21, 1, 25, 45, 505231, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inseminacion',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 10, 21, 1, 25, 48, 985684, tzinfo=utc)),
            preserve_default=False,
        ),
    ]