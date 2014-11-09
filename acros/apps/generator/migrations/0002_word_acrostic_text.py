# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='acrostic_text',
            field=models.CharField(default='ACROSTIC GOES HERE', max_length=200),
            preserve_default=True,
        ),
    ]
