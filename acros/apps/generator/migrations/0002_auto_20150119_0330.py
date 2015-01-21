# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acrostic',
            name='construction',
        ),
        migrations.RemoveField(
            model_name='acrostic',
            name='theme',
        ),
        migrations.AddField(
            model_name='acrostic',
            name='construction_sequence',
            field=models.CharField(max_length=200, default='P;A;VS;NS'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acrostic',
            name='tag_sequence',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acrostic',
            name='theme_name',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='value',
            field=models.FloatField(max_length=5, default=0),
        ),
    ]
