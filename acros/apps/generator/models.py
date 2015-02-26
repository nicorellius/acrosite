"""
file        :   models.py
date        :   2014-1101
module      :   generator
classes     :   Word, Theme, Construction, Acrostic, Score
description :   models for arostic generator
"""
import uuid

from django.db import models
# from django.contrib.auth.models import User

from common.models import BaseModel
from common.util import gen_uid


class Word(BaseModel):

    name = models.CharField(max_length=200, default='')
    valid_name_length = models.IntegerField(max_length=5, default=0)
    name_length = models.IntegerField(max_length=5, default=0)
    part_of_speech = models.CharField(max_length=200, default='NS')
    tags = models.CharField(max_length=200, blank=True)
    valuation = models.FloatField(default=-1.0, blank=True)  # a -1 flag implies "no valuation assigned"
    prevalence = models.IntegerField(max_length=1, default=0)  # values of 1, 2, 3 for general prevalence
    themes = models.CharField(max_length=1000, default='all')

    def get_valid_name_length(self):

        characters = list(str(self.name))
        counter = 0

        for character in characters:

            if (character.upper() in
                ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']):

                counter += 1

        return counter

    def get_name_length(self):

        return len(str(self.name))

    def save(self, *args, **kwargs):

        if not self.pk:

            self.valid_name_length = self.get_valid_name_length()
            self.name_length = self.get_name_length()
            super(Word, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Acrostic(BaseModel):

    uaid = models.CharField(max_length=10, default=gen_uid(10))
    vertical_word = models.CharField(max_length=200, default='shit')
    horizontal_words = models.CharField(max_length=200, default='so;happy;it\'s;thursday')
    theme_name = models.CharField(max_length=200, default='')
    construction_sequence = models.CharField(max_length=200, default='P;A;VS;NS')
    tag_sequence = models.CharField(max_length=200, default='')
    # when we need users to own acrostics
    # owner = models.ForeignKey(User)

    def save(self, *args, **kwargs):

        if not self.pk:

            self.uaid = gen_uid(10)
            super(Acrostic, self).save(*args, **kwargs)

    def __str__(self):
        
        component_words = self.horizontal_words.split(';')
        
        string = ''
        
        for word in component_words:
            string = ''.join([string, '\n', word])
            
        return string


class Score(BaseModel):

    value = models.FloatField(max_length=1, blank=True, default=0)
    mean = models.FloatField(max_length=2, blank=True, default=0)
    total = models.IntegerField(max_length=10, blank=True, default=0)
    acrostic = models.ForeignKey(Acrostic)

    def __str__(self):

        return str(self.value)
