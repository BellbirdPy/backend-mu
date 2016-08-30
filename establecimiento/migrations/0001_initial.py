# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-30 00:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('E', 'Expirado'), ('B', 'Borrado')], default='A', max_length=1)),
                ('fecha_expiracion', models.DateField()),
                ('miembros', models.ManyToManyField(blank=True, related_name='establecimientos', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='establecimientos_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(default='', max_length=50)),
                ('leido', models.BooleanField(default=False)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarea', to='establecimiento.Establecimiento')),
                ('usuario_asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarea_asignada', to=settings.AUTH_USER_MODEL)),
                ('usuario_creador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tarea_creada', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
