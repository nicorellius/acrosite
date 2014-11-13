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
from . import magic

# check out common/models.py for BaseModel definition
from common.models import BaseModel  # @UnresolvedImport

class Word(BaseModel):
    
    name = models.CharField(max_length=200)
    acrostic_text = models.CharField(max_length=200, default='ACROSTIC GOES HERE')
    
    def __str__(self):
        return self.name
    
    def generate_acrostic(self):
        if self.name.lower() == 'SHIT'.lower():
            self.acrostic_text = 'So Happy It\'s Thursday'
        elif self.name.lower() == 'EBOLA'.lower():
            self.acrostic_text = 'Everybody Believes in Ongoing Love, Africa!'
        else:
            self.acrostic_text = 'Sorry, we could not generate an acrostic for your submission.'
        return self.acrostic_text
    
class Acrostic(BaseModel):
    
    '''
    The vertical word formed by taking the first letter of every
    component word or phrase in the acrostic.
    '''
    vertical_word = models.CharField(max_length=200, default = 'N/A')
    
    '''
    The list of words or phrases that construct the acrostic.
    Words are separated by a semicolon.
    
    '''
    component_words = models.CharField(max_length=200, default = 'N/A')
    
    '''
    Refers to one or more acceptable sentence/phrase constructions associated
    with this acrostic.
    Each string is the name of a predefined group of grammatical constructions.
    '''
    construction = models.CharField(max_length=200, default = 'Anything')
    
    '''
    String describing the theme of the acrostic.  for example,
    cute animals
    Shakespearean dialect
    political
    each acrostic theme corresponds to a set of word libraries and 
    constructions.
    '''
    theme = models.CharField(max_length=200, default= 'ALL_CATEGORIES')
    
    def __str__(self):
        component_words = self.component_words.split(';')
        for word in component_words:
            str = str + word + '\n'
        return str
    
    def generate_random_acrostic(self, vert_word):
        self.vertical_word = vert_word
        
        print(magic.get_format(vert_word)) 
        
        if vert_word.upper() == 'TEST':
            self.component_words = "Take;Every;Single;Tangerine"
        
        return self.component_words