# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('usu_id', models.IntegerField()),
                ('pro_id', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('fechahora', models.DateTimeField()),
                ('comentario', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
