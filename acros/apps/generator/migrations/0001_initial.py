# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acrostic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(verbose_name='create date', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('slug', models.SlugField(help_text='slug for URLs')),
                ('description', models.TextField(blank=True)),
                ('vertical_word', models.CharField(max_length=200, default='N/A')),
                ('component_words', models.CharField(max_length=200, default='N/A')),
                ('construction', models.CharField(max_length=200, default='Anything')),
                ('theme', models.CharField(max_length=200, default='ALL_CATEGORIES')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(verbose_name='create date', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('slug', models.SlugField(help_text='slug for URLs')),
                ('description', models.TextField(blank=True)),
                ('name', models.CharField(max_length=200)),
                ('acrostic_text', models.CharField(max_length=200, default='ACROSTIC GOES HERE')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
