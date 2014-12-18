"""
file        :   models.py
date        :   2014-1101
module      :   generator
classes     :   Word
description  :   models for word generator
"""

from django.db import models

# check out common/models.py for BaseModel definition
from common.models import BaseModel


class Word(BaseModel):
    
    name = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=200, default='NN')
    tags = models.CharField(max_length=200, default='')
    valuation = models.FloatField(default=-1.0)  # a -1 flag implies "no valuation assigned"
    # prevalence = models.IntegerField(max_length=1, default=0)  # values of 1, 2, 3 for general prevalence
    # themes = models.CharField(max_length=200, default='politics')
    
    def __str__(self):

        string = ''.join([self.name, '\n', self.part_of_speech, '\n', 'tags:\n'])
        
        tags_array = self.tags.split(';')
        
        for tag in tags_array:
            string = ''.join([string, '\t', tag, '\n'])

        string = ''.join([string, 'valuation: ', self.valuation])
        
        return string


class Construction(BaseModel):
    
    sequence = models.CharField(max_length=200)
    themes = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    
    def __str__(self):
        return ''.join([self.constr_id, ':\n', self.sequence])
    
    def get_list(self):
        return self.sequence.split(';')


class Acrostic(BaseModel):
    
    vertical_word = models.CharField(max_length=200, default='N/A')
    horizontal_words = models.CharField(max_length=200, default='N;/;A')
    construction_id = models.CharField(max_length=200, default='Anything')
    theme = models.CharField(max_length=200, default='ALL_CATEGORIES')
    
    def __str__(self):
        
        component_words = self.horizontal_words.split(';')
        
        string = ''
        
        for word in component_words:
            string = ''.join([string, '\n', word])
            
        return string