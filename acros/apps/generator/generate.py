"""
file        :   generate.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   Generate an acrostic based on various inputs and the database of words.
"""

import random
import re

from .populate import subject_database, all_subject_databases
# from .populate import populate_database

from .models import Word, Acrostic, Theme



def generate_random_acrostic(vert_word, theme_name, *args):

    #TODO: retrieve the pre-generated theme based on its name
    theme = Theme()
    theme.name = theme_name

    acrostic = Acrostic()
    acrostic.vertical_word = vert_word
    
    if len(args) == 1:
        construction = args[0].get_list()
    
    # TODO: populate word table database appropriately
    # build word database if no words currently in database.
    # Word.objects.all().delete()
    
    if not Word.objects.all():
        
        #default settings
        if (theme_name == 'Select an Acrostic Theme'):
            theme_name = 'cute_animals'

        print("rebuilding entire database.")
        themes = [
                  "cute_animals",
                  "politics",
                  "sports",
                  "economics",
                  "current_events",
                  "movies",
                  "books_literature",
                  "explicit",
                  "religion",
                  ]
        
        all_subject_databases(themes)

        #print("repopulating database with theme {0}".format(theme_name))
        #subject_database('resources/{0}.txt'.format(theme_name))
            
    characters = list(vert_word)  # returns array of characters

    horz_words = ''

    counter = 0

    for letter in characters:
        
        if len(args) == 0:
            available_words = Word.objects.filter(
                themes__contains=theme_name,
                name__startswith=letter,
            )

        elif len(args) == 1:
            available_words = (Word.objects.filter(
                themes__contains=theme_name,                     
                name__startswith=letter,
                part_of_speech=construction[counter])
            )
        
        else:
            # default - only filter by letter (theme agnostic)
            available_words = Word.objects.filter(
                name__startswith=letter
            )
            
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
