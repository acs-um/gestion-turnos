# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0002_auto_20150601_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='notificado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
