# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-15 20:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0003_auto_20161010_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='establecimiento',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 10, 15, 20, 31, 59, 727843, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
