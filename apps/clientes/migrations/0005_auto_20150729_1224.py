# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20150608_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documento', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('obrasocial', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('clave', models.CharField(max_length=50)),
                ('reingresarclave', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='perfilcliente',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='PerfilCliente',
        ),
    ]
