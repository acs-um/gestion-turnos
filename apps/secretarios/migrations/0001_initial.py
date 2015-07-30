# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secretario',
            fields=[
                ('sec_id', models.AutoField(serialize=False, primary_key=True)),
                ('sec_nombre', models.CharField(max_length=50)),
                ('sec_apellido', models.CharField(max_length=50)),
                ('sec_documento', models.IntegerField()),
                ('sec_telefono', models.IntegerField()),
                ('sec_email', models.EmailField(max_length=75)),
                ('sec_pass', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
