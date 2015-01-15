"""
file        :   generate.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   Generate an acrostic based on various inputs and the database of words.
"""

import random
import re

from .populate import populate_database
# from .populate import populate_database

from .models import Word, Acrostic, Theme
from django.db.models import Q


def generate_random_acrostic(vert_word, theme_name, *args):

    acrostic = Acrostic()
    acrostic.vertical_word = vert_word
    
    if len(args) == 1:
        construction = args[0].get_list()
    
    # TODO: populate word table before this screen
    # build word database if no words currently in database.
    # Word.objects.all().delete()

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

    # if no theme is specified, choose one at random.
    if theme_name == 'Select an Acrostic Theme':
        theme_name = random.choice(themes)
        print('Theme randomly selected to {0}'.format(theme_name))
    
    if not Word.objects.all():
        
        print("Rebuilding entire database...")
          
        populate_database(themes)

        # print("repopulating database with theme {0}".format(theme_name))
        # subject_database('resources/{0}.txt'.format(theme_name))
            
    characters = list(vert_word)  # returns array of characters

    horz_words = ''

    counter = 0
    # general = 'books_literature'
    all_themes = "all"
    for letter in characters:
        
        if len(args) == 0:
            available_words = Word.objects.filter(
                Q(themes__contains=theme_name) | Q(themes__contains=all_themes),
                Q(name__startswith=letter),
            )

        elif len(args) == 1:
            available_words = Word.objects.filter(
                Q(name__startswith=letter),
                Q(part_of_speech=construction[counter]),
                Q(themes__contains=theme_name) | Q(themes__contains=all_themes),
            )
        
        else:
            available_words = Word.objects.filter(
                Q(name__startswith=letter)
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

    print("Acrostic:\n", acrostic.__str__())

    return acrostic
