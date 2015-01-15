"""
file        :   models.py
date        :   2014-1101
module      :   generator
classes     :   Word, Theme, Construction, Acrostic, Score
description :   models for arostic generator
"""

from django.db import models
from django.contrib.auth.models import User

# check out common/models.py for BaseModel definition
from common.models import BaseModel


class Word(BaseModel):
    
    name = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=200, default='NS')
    tags = models.CharField(max_length=200, default='')
    valuation = models.FloatField(default=-1.0)  # a -1.0 flag implies "no valuation assigned"
    prevalence = models.IntegerField(max_length=1, default=0)  # values of 1, 2, 3 for general prevalence
    themes = models.CharField(max_length=1000, default='all')
    
    def __str__(self):

        string = ''.join([self.name, '\n', self.part_of_speech, '\n', 'tags:\n'])
        
        tags_array = self.tags.split(';')
        
        for tag in tags_array:
            string = ''.join([string, '\t', tag, '\n'])

        string = ''.join([string, 'valuation: ', str(self.valuation)])
        
        return string


class Theme(BaseModel):

    name = models.CharField(max_length=200, default='default theme')
    group = models.CharField(max_length=200, blank=True, default='main')
    tags = models.CharField(max_length=200, blank=True, default='')
    # words = models.CharField(max_length=1000)  # themes should be part of word not this way


class Construction(BaseModel):
    
    sequence = models.CharField(max_length=200, unique=True)
    themes = models.CharField(max_length=200)
    tags = models.CharField(max_length=200, blank=True, default='')
    type = models.CharField(max_length=200, blank=True, default='')
    
    def __str__(self):
        return ''.join([self.sequence, ' | ', self.description])
    
    def get_list(self):
        return self.sequence.split(';')


class Acrostic(BaseModel):

    DEFAULT_THEME_ID = 1  # we should create a default theme called `all` with id of 1

    vertical_word = models.CharField(max_length=200, default='shit')
    horizontal_words = models.CharField(max_length=200, default='so;happy;it\'s;thursday')
    construction = models.OneToOneField(Construction, primary_key=True)
    theme = models.ForeignKey(Theme, default=DEFAULT_THEME_ID)
    
    def __str__(self):
        
        component_words = self.horizontal_words.split(';')
        
        string = ''
        
        for word in component_words:
            string = ''.join([string, '\n', word])
            
        return string


class Score(BaseModel):

    value = models.IntegerField(max_length=1, default=0)
    acrostic = models.ForeignKey(Acrostic)
    user = models.ForeignKey(User)