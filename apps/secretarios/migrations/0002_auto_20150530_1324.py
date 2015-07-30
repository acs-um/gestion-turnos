# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secretario',
            old_name='sec_apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='secretario',
            old_name='sec_nombre',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='secretario',
            old_name='sec_documento',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='secretario',
            old_name='sec_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='secretario',
            old_name='sec_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='secretario',
            old_name='sec_pass',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='secretario',
            old_name='sec_telefono',
            new_name='telefono',
        ),
        migrations.AddField(
            model_name='secretario',
            name='reingresarclave',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
