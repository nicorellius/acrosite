from django.db import models
from django.contrib.auth.models import User

from localflavor.us.forms import USPhoneNumberField


class UserProfile(models.Model):

    def upload_to(instance, filename):
        return 'images/avatars/{0}/{1}'.format(instance.user.username, filename)

    user = models.OneToOneField(User)
    organization = models.CharField(blank=True, default='Acrostic Tees, LLC')
    website = models.URLField(default='acrostictees.com')
    phone = USPhoneNumberField()
    avatar = models.ImageField(upload_to=upload_to, verbose_name="Avatar image")

    def __str__(self):
        return str(self.user)
