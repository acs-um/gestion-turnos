# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='cli_apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='cli_nombre',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='cli_documento',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='cli_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='cli_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='cli_obrasocial',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='cli_pass',
            new_name='obrasocial',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='cli_telefono',
            new_name='telefono',
        ),
        migrations.AddField(
            model_name='cliente',
            name='reingresarclave',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
