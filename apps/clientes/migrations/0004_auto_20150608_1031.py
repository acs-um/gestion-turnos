# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20150605_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfilcliente',
            old_name='cliente',
            new_name='usuario',
        ),
    ]
