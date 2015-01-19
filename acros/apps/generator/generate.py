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
from .filter_data import create_acrostic_filter_data

from .models import Word, Acrostic
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
            '''
            available_words = Word.objects.filter(
                Q(name__startswith=letter),
                Q(part_of_speech=construction[counter]),
                Q(themes__contains=theme_name) | Q(themes__contains=all_themes),
            )
            '''
            '''
            available_words = Word.objects.filter(
                Q(name__startswith=letter),
                Q(part_of_speech=construction[counter]),
                Q(themes__contains=theme_name),
            )
            '''
            
            filters = [
                       Q(name__startswith=letter),
                       Q(part_of_speech=construction[counter]),
                       Q(themes__contains=theme_name)
                       ]
            
            pre_filter = Word.objects.all()
        
            # progressively refine set - this is more efficient than chaining queries.
            # please see
            # https://docs.djangoproject.com/en/1.7/ref/models/querysets/#id4
            for filter_query in filters:
                post_filter = pre_filter.filter(filter_query)
                pre_filter = post_filter
                
            available_words = post_filter
            '''
            available_words = get_available_words(filters)
            '''
            
        
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

def generate_cute_animal_acrostic(vert_word, theme_name):
    
    # database rebuilding: for use with database file import testing
    # rebuild_database(True)
    # rebuild_database(False)
    
    filter_set_data = create_acrostic_filter_data(vert_word, theme_name)
    filter_sets = filter_set_data[0]
    construction_list = filter_set_data[1]
    tag_list = filter_set_data[2]
    
    horz_words = ''
    counter = 0
    characters = list(vert_word)
    
    for filter in filter_sets:
        
        pre_filter = Word.objects.all()
        
        for filter_query in filter:
            post_filter = pre_filter.filter(filter_query)
            pre_filter = post_filter
                
        available_words = post_filter

        if not available_words:
            horz_words = "{0}{1};".format(horz_words, characters[counter])

        else:
            w = random.choice(available_words)
            horz = re.sub('[_]', ' ', w.name)
            horz_words = "{0}{1};".format(horz_words, horz)

        counter += 1
        
    #Create Acrostic from all relevant data
    acrostic = Acrostic()
    acrostic.vertical_word = vert_word
    acrostic.horizontal_words = horz_words
    acrostic.theme_name = theme_name
    acrostic.construction_sequence = construction_list
    acrostic.tag_sequence = tag_list

    print("Acrostic:\n", acrostic.__str__())
    
    return acrostic

def rebuild_database(force_rebuild):
    
    if force_rebuild==True:
        Word.objects.all().delete()
    
    if not Word.objects.all():
        print("Rebuilding entire database...")
         
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
        
        populate_database(themes)
        
    return