# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.accounts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('slug', models.SlugField(help_text='slug for URLs')),
                ('description', models.TextField(blank=True)),
                ('organization', models.CharField(default='Acrostic Tees, LLC', blank=True, max_length=255)),
                ('website', models.URLField(default='acrostictees.com')),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('avatar', models.ImageField(verbose_name='Avatar image', upload_to=apps.accounts.models.UserProfile.upload_to)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Profiles',
            },
            bases=(models.Model,),
        ),
    ]
