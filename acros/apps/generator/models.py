"""
file        :   models.py
date        :   2014-1101
module      :   generator
classes     :   Word, Theme, Construction, Acrostic, Score
description :   models for arostic generator
"""
from django.db import models
# from django.contrib.auth.models import User

from common.models import BaseModel


class Word(BaseModel):

    name = models.CharField(max_length=200, default='')
    name_length = models.IntegerField(max_length=10, default = 0)
    part_of_speech = models.CharField(max_length=200, default='NS')
    tags = models.CharField(max_length=200, blank=True)
    valuation = models.FloatField(default=-1.0, blank=True)  # a -1 flag implies "no valuation assigned"
    prevalence = models.IntegerField(max_length=1, default=0)  # values of 1, 2, 3 for general prevalence
    themes = models.CharField(max_length=1000, default='all')
    
    def __str__(self):
        return self.name


class Acrostic(BaseModel):

    vertical_word = models.CharField(max_length=200, default='shit')
    horizontal_words = models.CharField(max_length=200, default='so;happy;it\'s;thursday')
    theme_name = models.CharField(max_length=200,default='')
    construction_sequence = models.CharField(max_length=200, default='P;A;VS;NS')
    tag_sequence = models.CharField(max_length=200, default='')
    # when we need users to own acrostics
    # owner = models.ForeignKey(User)

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
