# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('tur_id', models.AutoField(serialize=False, primary_key=True)),
                ('tur_usu_id', models.IntegerField()),
                ('tur_estado', models.CharField(max_length=50)),
                ('tur_fechahora', models.DateTimeField()),
                ('tur_comentario', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usu_id', models.AutoField(serialize=False, primary_key=True)),
                ('usu_rol', models.CharField(max_length=50)),
                ('usu_email', models.EmailField(max_length=75)),
                ('usu_pass', models.CharField(max_length=50)),
                ('usu_nombre', models.CharField(max_length=50)),
                ('usu_apellido', models.CharField(max_length=50)),
                ('usu_telefono', models.IntegerField()),
                ('usu_dni', models.IntegerField()),
                ('usu_direccion', models.CharField(max_length=50)),
                ('usu_obrasocial', models.CharField(max_length=50)),
                ('usu_estado', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
