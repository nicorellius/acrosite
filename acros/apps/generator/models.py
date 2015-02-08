"""
file        :   models.py
date        :   2014-1101
module      :   generator
classes     :   Word, Theme, Construction, Acrostic, Score
description :   models for arostic generator
"""
import re

from django.utils.text import slugify
from django.db import models
# from django.contrib.auth.models import User

# check out common/models.py for BaseModel definition
from common.models import BaseModel


class Word(BaseModel):
    
    name = models.CharField(max_length=200, default='')
    part_of_speech = models.CharField(max_length=200, default='NN')
    tags = models.CharField(max_length=200, blank=True)
    valuation = models.FloatField(default=-1.0, blank=True)  # a -1 flag implies "no valuation assigned"
    prevalence = models.IntegerField(max_length=1, default=0)  # values of 1, 2, 3 for general prevalence
    themes = models.CharField(max_length=200, default='politics')
    
    def __str__(self):

        string = ''.join([self.name, '\n', self.part_of_speech, '\n', 'tags:\n'])
        
        tags_array = self.tags.split(';')
        
        for tag in tags_array:
            string = ''.join([string, '\t', tag, '\n'])

        string = ''.join([string, 'valuation: ', str(self.valuation)])
        
        return string


# class Theme(BaseModel):
#
#     name = models.CharField(max_length=200, default='default')
#     group = models.CharField(max_length=200, default='main')
#     tags = models.CharField(max_length=200, blank=True)


class Construction(BaseModel):

    sequence = models.CharField(max_length=200, default='A;A;A;NP;')
    themes = models.CharField(max_length=200, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return ''.join([self.sequence, ' | ', self.description])

    def get_list(self):
        return self.sequence.split(';')


class Acrostic(BaseModel):
    
    vertical_word = models.CharField(max_length=200, default='shit')
    horizontal_words = models.CharField(max_length=200, default='so;happy;it\s;thursday')
    construction = models.CharField(max_length=200, default='A;A;NV;N')
    theme = models.CharField(max_length=200, default='offensive')
    # when we need users to own acrostics
    # owner = models.ForeignKey(User)
    
    def __str__(self):
        
        component_words = self.horizontal_words.split(';')
        
        string = ''
        
        for word in component_words:
            string = ''.join([string, '\n', word])
            
        return string

    def save(self, **kwargs):

        slugify(re.sub(';', ' ', self.horizontal_words))

        super(BaseModel, self).save(**kwargs)


class Score(BaseModel):

    value = models.FloatField(max_length=1, blank=True, default=0)
    mean = models.FloatField(max_length=2, blank=True, default=0)
    total = models.IntegerField(max_length=10, blank=True, default=0)
    acrostic = models.ForeignKey(Acrostic)

    def __str__(self):

        return str(self.value)