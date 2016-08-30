# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-30 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0001_initial'),
        ('lote', '0001_initial'),
        ('establecimiento', '0001_initial'),
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePalpacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.BooleanField()),
                ('gestacion', models.CharField(blank=True, max_length=8, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_palpaciones', to='animal.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Palpacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo', models.CharField(choices=[('M', 'Manual'), ('E', 'Ecografo')], default='M', max_length=1)),
                ('fecha', models.DateField()),
                ('cantidad_prenados', models.IntegerField()),
                ('cantidad_total', models.IntegerField()),
                ('animales_prenados', models.ManyToManyField(related_name='palpaciones', to='animal.Animal')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='palpaciones', to='establecimiento.Establecimiento')),
                ('lote', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='palpaciones', to='lote.Lote')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='palpaciones', to='servicio.Servicio')),
            ],
        ),
        migrations.AddField(
            model_name='detallepalpacion',
            name='palpacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='palpacion.Palpacion'),
        ),
    ]
