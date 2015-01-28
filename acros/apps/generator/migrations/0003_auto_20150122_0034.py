# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_auto_20150119_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='sequence',
            field=models.CharField(unique=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='word',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='word',
            name='part_of_speech',
            field=models.CharField(default='NS', max_length=20),
        ),
        migrations.AlterField(
            model_name='word',
            name='tags',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
