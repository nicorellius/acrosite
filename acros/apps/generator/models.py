"""
file        :   models.py
date        :   2014-1101
module      :   generator
classes     :   Word
desription  :   models for word generator
"""

from django.db import models

# check out common/models.py for BaseModel definition
from common.models import BaseModel  # @UnresolvedImport

class Word(BaseModel):
    
    name = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=200,default="NN")
    tags = models.CharField(max_length=200,default="")
    valuation = models.FloatField(default=-1.0) #a -1 flag implies "no valuation assigned"
    
    def __str__(self):
        str = (self.name + "\n"
               + self.part_of_speech + "\n"
               + "tags:\n")
        tags_array = self.tags.split(';')
        for tag in tags_array:
            str = str + "\t" + tag + "\n"
        str = str + "valuation: " + self.valuation
        return str
    
class Construction(BaseModel):
    construction = models.CharField(max_length=200)
    construction_id = models.CharField(max_length=200, default= 'Anything')    
    
class Acrostic(BaseModel):
    
    vertical_word = models.CharField(max_length=200, default = 'N/A')
    horizontal_words = models.CharField(max_length=200, default = 'N;/;A')
    construction_id = models.CharField(max_length=200, default= 'Anything')
    theme = models.CharField(max_length=200, default= 'ALL_CATEGORIES')
    
    def __str__(self):
        component_words = self.horizontal_words.split(';')
        str = ""
        for word in component_words:
            str = str + "\n" + word
        return str