# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('slug', models.SlugField(help_text='slug for URLs')),
                ('description', models.TextField(blank=True)),
                ('sequence', models.CharField(max_length=200)),
                ('themes', models.CharField(max_length=200)),
                ('tags', models.CharField(blank=True, default='', max_length=200)),
                ('type', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Acrostic',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('slug', models.SlugField(help_text='slug for URLs')),
                ('description', models.TextField(blank=True)),
                ('vertical_word', models.CharField(default='N/A', max_length=200)),
                ('horizontal_words', models.CharField(default='N;/;A', max_length=200)),
                ('construction', models.OneToOneField(primary_key=True, to='generator.Construction', serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('slug', models.SlugField(help_text='slug for URLs')),
                ('description', models.TextField(blank=True)),
                ('value', models.IntegerField(default=0, max_length=1)),
                ('acrostic', models.ForeignKey(to='generator.Acrostic')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('slug', models.SlugField(help_text='slug for URLs')),
                ('description', models.TextField(blank=True)),
                ('name', models.CharField(default='default theme', max_length=200)),
                ('group', models.CharField(blank=True, default='main', max_length=200)),
                ('tags', models.CharField(blank=True, default='', max_length=200)),
                ('words', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('slug', models.SlugField(help_text='slug for URLs')),
                ('description', models.TextField(blank=True)),
                ('name', models.CharField(max_length=200)),
                ('part_of_speech', models.CharField(default='NN', max_length=200)),
                ('tags', models.CharField(default='', max_length=200)),
                ('valuation', models.FloatField(default=-1.0)),
                ('prevalence', models.IntegerField(default=0, max_length=1)),
                ('themes', models.CharField(default='politics', max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='acrostic',
            name='theme',
            field=models.ForeignKey(to='generator.Theme', default=1),
            preserve_default=True,
        ),
    ]
