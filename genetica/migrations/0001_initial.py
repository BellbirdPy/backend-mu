# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-30 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuracion', '0001_initial'),
        ('lote', '0001_initial'),
        ('establecimiento', '0001_initial'),
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalGenetica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('nombre_corto', models.CharField(blank=True, max_length=32, null=True)),
                ('porcentaje_pureza', models.PositiveIntegerField(choices=[(25, 25), (50, 50), (75, 75), (100, 100)])),
                ('tipo_servicio', models.CharField(choices=[('MN', 'Monta Natural'), ('IA', 'Inceminacion Artificial')], max_length=2)),
                ('rp', models.CharField(blank=True, max_length=32, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('cantidad_pajuelas', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('pedigree_padre', models.CharField(blank=True, max_length=32, null=True)),
                ('pedigree_madre', models.CharField(blank=True, max_length=32, null=True)),
                ('pedigree_abuelo', models.CharField(blank=True, max_length=32, null=True)),
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_genetica', to='establecimiento.Establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='LoteGenetica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje_pureza', models.PositiveIntegerField(choices=[(25, 25), (50, 50), (75, 75), (100, 100)])),
                ('tipo_servicio', models.CharField(choices=[('MN', 'Monta Natural'), ('IA', 'Inceminacion Artificial')], max_length=2)),
                ('carimbo', models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('descripcion', models.TextField()),
                ('pedigree_padre', models.CharField(max_length=32)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Categoria')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lote_genetica', to='establecimiento.Establecimiento')),
                ('lote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lote.Lote')),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Raza')),
            ],
        ),
        migrations.AddField(
            model_name='animalgenetica',
            name='lote_genetica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animal_genetica', to='genetica.LoteGenetica'),
        ),
    ]
