# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='create date', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('slug', models.SlugField(help_text='slug for URLs')),
                ('description', models.TextField(blank=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
