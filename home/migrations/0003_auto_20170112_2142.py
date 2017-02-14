# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-13 00:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170112_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL),
        ),
    ]