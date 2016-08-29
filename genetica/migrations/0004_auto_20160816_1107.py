# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-16 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genetica', '0003_auto_20160815_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalgenetica',
            name='cantidad_pajuelas',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='animalgenetica',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='animalgenetica',
            name='nombre',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='animalgenetica',
            name='nombre_corto',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='animalgenetica',
            name='pedigree_abuelo',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='animalgenetica',
            name='pedigree_madre',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='animalgenetica',
            name='pedigree_padre',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='animalgenetica',
            name='porcentaje_pureza',
            field=models.PositiveIntegerField(choices=[(25, 25), (50, 50), (75, 75), (100, 100)]),
        ),
        migrations.AlterField(
            model_name='animalgenetica',
            name='rp',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='lotegenetica',
            name='porcentaje_pureza',
            field=models.PositiveIntegerField(choices=[(25, 25), (50, 50), (75, 75), (100, 100)]),
        ),
    ]