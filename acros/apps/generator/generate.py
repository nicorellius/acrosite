"""
file        :   generate.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   Generate an acrostic based on various inputs and the database of words.
"""

from .populate import basic_list
from .models import Word, Acrostic
import random

def generate_random_acrostic(vert_word):
   
    acrostic = Acrostic()
    acrostic.vertical_word = vert_word
    
    #build word database if no words currently in database.
    if not Word.objects.all():
        basic_list()
            
    characters = list(vert_word) #returns array of characters
    horz_words = ""
    for letter in characters:
                
        #filter list appropriately
        availableWords = Word.objects.filter(name__startswith=letter)
                
        if not availableWords:
            horz_words = horz_words + letter + ";"
        else:
            w = random.choice(availableWords)
            horz_words = horz_words + w.name + ";"
    
    acrostic.vertical_word = vert_word
    acrostic.horizontal_words = horz_words
    print("Acrostic:\n", acrostic.__str__());
    return acrostic
        
