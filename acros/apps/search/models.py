from django.db import models

from apps.generator.models import Word


class WordListSearch(models.Model):
    keyword = models.CharField(max_length=50)
    word = models.ForeignKey(Word)

    def __unicode__(self):
        return self.keyword
