# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='part_of_speech',
            field=models.CharField(max_length=200, default='NS'),
        ),
        migrations.AlterField(
            model_name='word',
            name='themes',
            field=models.CharField(max_length=1000, default='politics'),
        ),
    ]
