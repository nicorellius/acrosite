"""
file        :   generate.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   Generate an acrostic based on various inputs and the database of words.
"""

import random
import re

from .populate import populate_database,import_alpha_list
# from .populate import populate_database
from .filter_data import create_acrostic_filter_data

from .models import Word, Acrostic
from django.db.models import Q
    
def generate_random_acrostic(vert_word, theme_name):
    
    # database rebuilding: for use with database file import testing
    # rebuild_database(True)
    # rebuild_database(False)
    
    filter_set_data = create_acrostic_filter_data(vert_word, theme_name)
    filter_sets = filter_set_data[0]
    construction_list = filter_set_data[1]
    tag_list = filter_set_data[2]
    
    horz_words = ''
    horz_list = []
    counter = 0
    characters = list(vert_word)
    
    for filter in filter_sets:
        
        #initial state- all objects
        pre_filter = Word.objects.all()
        
        # filter based on construction and vertical word
        for filter_query in filter:
            post_filter = pre_filter.filter(filter_query)
            pre_filter = post_filter
        
        #handle duplicates - disallow duplicates unless the entire filtered list has been exhausted
        available_words = list(post_filter)
        duplicate_filtered = list(available_words)
        for word in available_words:
            if word in horz_list:
                duplicate_filtered.remove(word)
        
        if not duplicate_filtered:
            duplicate_filtered = available_words
        
        # if no words remain after all filters have been applied, return an empty character
        if not duplicate_filtered:
            horz_words = "{0}{1};".format(horz_words, characters[counter])

        # select a word at random
        else:
            w = random.choice(duplicate_filtered)
            horz_list.append(w)
            
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
        '''
        themes = [
        "cute_animals",
        "politics",
        ] 
        
        populate_database(themes)
        '''
        
        import_alpha_list();
        
        
    return