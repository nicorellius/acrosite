"""
file        :   models.py
date        :   2014-1215
module      :   accounts
classes     :   UserProfile
description  :   database fields for accounts module, including user profile
"""

import datetime

from django import forms
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.files.images import get_image_dimensions

from common.models import BaseModel


class UserProfile(BaseModel):

    def upload_to(instance, filename):
        return 'images/avatars/{0}/{1}'.format(instance.user.username, filename)

    user = models.OneToOneField(User)
    organization = models.CharField(blank=True, max_length=255, default='Acrostic Tees, LLC')
    website = models.URLField(default='acrostictees.com')
    phone = models.CharField(blank=True, max_length=12)
    avatar = models.ImageField(upload_to=upload_to, verbose_name="Avatar image")

    class Meta:
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return str(self.user)

    def was_created_recently(self):
        return self.create_date >= timezone.now() - datetime.timedelta(days=1)

    # borrowed from here: http://stackoverflow.com/questions/6396442/add-image-avatar-to-users-in-django
    def clean_avatar(self):

        avatar = self.cleaned_data['avatar']

        try:
            width, height = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 100

            if width > max_width or height > max_height:

                raise forms.ValidationError(
                    # u'Image must be {0} x {1} pixels or smaller.'.format(max_width, max_height)
                    _('Image must be correct dimensions: %(max_width)s x %(max_height)s'),
                    code='invalid',
                    params={
                        'max_width': max_width,
                        'max_height': max_height,
                    },
                )

            # validate content type
            main, sub = avatar.content_type.split('/')

            if not (main == 'image' and sub in base.IMAGE_FORMAT):  # ['jpeg', 'pjpeg', 'gif', 'png']):

                raise forms.ValidationError('Please use a JPG, GIF or PNG image.')

            # IMAGE_FORMAT = ('.png','.gif','.jpg','.jpeg')

            # validate file size
            if len(avatar) > (20 * 1024):

                raise forms.ValidationError(
                    _('Avatar file size may not exceed 20 Kb.'))

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
