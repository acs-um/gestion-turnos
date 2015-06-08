# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesional',
            old_name='pro_apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='profesional',
            old_name='pro_nombre',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='profesional',
            old_name='pro_documento',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='profesional',
            old_name='pro_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='profesional',
            old_name='pro_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='profesional',
            old_name='pro_especialidad',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='profesional',
            old_name='pro_pass',
            new_name='especialidad',
        ),
        migrations.RenameField(
            model_name='profesional',
            old_name='pro_telefono',
            new_name='telefono',
        ),
        migrations.AddField(
            model_name='profesional',
            name='reingresarclave',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
