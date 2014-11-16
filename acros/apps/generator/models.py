"""
file        :   models.py
date        :   2014-1101
module      :   generator
classes     :   Word
desription  :   models for word generator
"""

from django.db import models
#from magic import get_format 
# @UnresolvedImport
from . import magic #@UnresolvedImport

# check out common/models.py for BaseModel definition
from common.models import BaseModel  # @UnresolvedImport

class Word(BaseModel):
    
    name = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=200)
    themes = models.CharField(max_length=200)
    valuation = models.FloatField()
    
    def __str__(self):
        return self.name
    
class Acrostic(BaseModel):
    
    vertical_word = models.CharField(max_length=200, default = 'N/A')
    horizontal_words = models.CharField(max_length=200, default = 'N;/;A')
    construction = models.CharField(max_length=200)
    construction_name = models.CharField(max_length=200, default= 'Anything')
    theme = models.CharField(max_length=200, default= 'ALL_CATEGORIES')
    
    def __str__(self):
        component_words = self.horizontal_words.split(';')
        str = ""
        for word in component_words:
            str = str + word + "\n"
        return str
    
    def generate_random_acrostic(self, vert_word):
        self.vertical_word = vert_word
        
        print("Part of speech: ", magic.get_format(vert_word)) 
        
        if vert_word.upper() == 'TEST':
            self.horizontal_words = "Take;Every;Single;Tangerine"
        else:
            self.horizontal_words = "A;B;C"
        print("Acrostic: ", self.horizontal_words);
        return self.horizontal_words