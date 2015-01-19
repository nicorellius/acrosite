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
    
    name = models.CharField(max_length=100)
    part_of_speech = models.CharField(max_length=20, default='NS')
    tags = models.CharField(max_length=1000, default='')
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
    
    sequence = models.CharField(max_length=1000, unique=True)
    themes = models.CharField(max_length=200)
    tags = models.CharField(max_length=200, blank=True, default='')
    type = models.CharField(max_length=200, blank=True, default='')
    
    def __str__(self):
        return ''.join([self.sequence, ' | ', self.description])
    
    def get_list(self):
        list_with_empty = self.sequence.split(';')
        return [i for i in list_with_empty if i != '']


class Acrostic(BaseModel):

    vertical_word = models.CharField(max_length=200, default='shit')
    horizontal_words = models.CharField(max_length=200, default='so;happy;it\'s;thursday')
    theme_name = models.CharField(max_length=200,default='')
    construction_sequence = models.CharField(max_length=200, default='P;A;VS;NS')
    tag_sequence = models.CharField(max_length=200, default='')
    
    def __str__(self):
        
        component_words = self.horizontal_words.split(';')
        
        string = ''
        
        for word in component_words:
            string = ''.join([string, '\n', word])
            
        return string


class Score(BaseModel):

    value = models.FloatField(max_length=5, default=0)
    acrostic = models.ForeignKey(Acrostic)
    user = models.ForeignKey(User)