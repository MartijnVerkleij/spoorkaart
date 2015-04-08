# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('tel_code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('location_lat', models.DecimalField(max_digits=13, decimal_places=10)),
                ('location_lon', models.DecimalField(max_digits=13, decimal_places=10)),
                ('tracks', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.IntegerField(default=1)),
                ('station_1', models.ForeignKey(related_name='station1', to='railgraph.Station')),
                ('station_2', models.ForeignKey(related_name='station2', to='railgraph.Station')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
