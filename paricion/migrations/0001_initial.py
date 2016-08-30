# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-30 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0001_initial'),
        ('palpacion', '0001_initial'),
        ('lote', '0001_initial'),
        ('establecimiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paricion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('aborto', models.BooleanField(default=False)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pariciones', to='establecimiento.Establecimiento')),
                ('hijo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nacimiento', to='animal.Animal')),
                ('lote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pariciones', to='lote.Lote')),
                ('madre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pariciones', to='animal.Animal')),
                ('palpacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pariciones', to='palpacion.Palpacion')),
            ],
        ),
    ]
