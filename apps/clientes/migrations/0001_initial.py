# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_id', models.AutoField(serialize=False, primary_key=True)),
                ('cli_nombre', models.CharField(max_length=50)),
                ('cli_apellido', models.CharField(max_length=50)),
                ('cli_documento', models.IntegerField()),
                ('cli_telefono', models.IntegerField()),
                ('cli_obrasocial', models.CharField(max_length=50)),
                ('cli_email', models.EmailField(max_length=75)),
                ('cli_pass', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
