# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0002_auto_20150530_1324'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='pro_id',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='usu_id',
        ),
        migrations.AddField(
            model_name='turno',
            name='pro',
            field=models.ForeignKey(default=1, to='profesionales.Profesional'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turno',
            name='usu',
            field=models.ForeignKey(default=2, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
