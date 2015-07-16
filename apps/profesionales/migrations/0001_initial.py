# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('pro_id', models.AutoField(serialize=False, primary_key=True)),
                ('pro_nombre', models.CharField(max_length=50)),
                ('pro_apellido', models.CharField(max_length=50)),
                ('pro_documento', models.IntegerField()),
                ('pro_telefono', models.IntegerField()),
                ('pro_especialidad', models.CharField(max_length=50)),
                ('pro_email', models.EmailField(max_length=75)),
                ('pro_pass', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
