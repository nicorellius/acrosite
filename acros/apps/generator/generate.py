"""
file        :   generate.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   Generate an acrostic based on various inputs and the database of words.
"""

import random, re

from .populate import populate_database, subject_database
from .models import Word, Acrostic


def generate_random_acrostic(vert_word, *args):
   
    acrostic = Acrostic()
    acrostic.vertical_word = vert_word
    
    if len(args) == 1:
        construction = args[0].get_list()
    
    #build word database if no words currently in database.
    if not Word.objects.all(): # @UndefinedVariable
        print("populating database...")
        #populate_database()
        subject_database('resources/CuteAnimals.txt')
            
    characters = list(vert_word) #returns array of characters
    horz_words = ""
    counter = 0
    for letter in characters:
        
        if len(args) == 0:
            available_words = Word.objects.filter(name__startswith=letter) # @UndefinedVariable
        elif len(args) == 1:
            available_words = (Word.objects.filter( # @UndefinedVariable
                              name__startswith=letter,
                              part_of_speech=construction[counter]))
        else:
            #default - only filter by letter
            available_words = Word.objects.filter(name__startswith=letter) # @UndefinedVariable
            
        if not available_words:
            horz_words = "{0}{1};".format(horz_words, letter)
        else:
            w = random.choice(available_words)
            horz = re.sub('[_]', ' ', w.name)
            horz_words = "{0}{1};".format(horz_words, horz)
        counter += 1
        
    acrostic.vertical_word = vert_word
    acrostic.horizontal_words = horz_words
    print("Acrostic:\n", acrostic.__str__());
    return acrostic        
