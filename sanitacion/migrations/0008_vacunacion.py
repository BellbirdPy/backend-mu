# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0007_auto_20160519_2134'),
        ('sanitacion', '0007_auto_20160517_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vacunacion', models.DateField()),
                ('nombre', models.CharField(default='', max_length=50)),
                ('nombre_cientifico', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('veterinario', models.CharField(default='', max_length=40)),
                ('enfermedad', models.CharField(default='', max_length=30)),
                ('codigo', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacunaciones', to='establecimiento.Establecimiento')),
            ],
        ),
    ]
