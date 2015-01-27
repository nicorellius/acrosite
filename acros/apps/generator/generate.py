"""
file        :   generate.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   Generate an acrostic based on various inputs and the database of words.
"""

import random
import re

from .populate import import_alpha_list
from .build_construction import create_acrostic_data

from .models import Word, Acrostic
    
def generate_random_acrostic(vert_word, theme_name):
    
    # database rebuilding: for use with database file import testing
    # rebuild_database(True)
    # rebuild_database(False)
    
    #master list of available options
    construction_dictionary = {
        'cute_animals':[1,2,3,4],
        'politics':[1,2,3,4],
        'music':[1,2,3,4],
        }
    
    construction_id_list = construction_dictionary[theme_name]
    
    build_or_rebuild_required = True
    
    while build_or_rebuild_required:
        build_or_rebuild_required = False
        
        construction_type = random.choice(construction_id_list)
        
        filter_set_data = create_acrostic_data(vert_word, theme_name, construction_type)
        filter_sets = filter_set_data[0]
        construction_list = filter_set_data[1]
        tag_list = filter_set_data[2]
    
        horz_words = ''
        horz_word_list = []
        counter = 0
        characters = list(vert_word)
    
        for filter_set in filter_sets:
        
            #initial state- all objects
            pre_filter = Word.objects.all()
        
            # filter based on construction and vertical word
            for filter_query in filter_set:
                post_filter = pre_filter.filter(filter_query)
                pre_filter = post_filter
        
            #handle duplicates - disallow duplicates unless the entire filtered list has been exhausted
            available_words = list(post_filter)
            duplicate_filtered = list(available_words)
            for word in available_words:
                if word in horz_word_list:
                    duplicate_filtered.remove(word)
        
            if not duplicate_filtered:
                duplicate_filtered = available_words
        
            # if no words remain after all filters have been applied, try a different construction
            # if no construction works, return an empty character.
            if not duplicate_filtered:
                if len(construction_id_list) == 1:
                    horz_words = "{0}{1};".format(horz_words, characters[counter])
                else:
                    build_or_rebuild_required = True
                    construction_id_list.remove(construction_type)
                    break


            # select a word at random
            else:
                w = random.choice(duplicate_filtered)
                horz_word = re.sub('[_]', ' ', w.name)
                horz_word_list.append(horz_word)
            
                #horz_words = "{0}{1};".format(horz_words, horz_word)

            counter += 1
       
    #Post-acrostic modifications
    counter = 1
    period_to_last = False
    while counter < len(horz_word_list):
        chars = list(horz_word_list[counter])
        if chars[len(chars) - 1] == ',':
            horz_word_list[counter-1] = '{0}.'.format(horz_word_list[counter-1])
            period_to_last = True
        counter += 1
        
    if period_to_last:
        if horz_word_list[counter-1] != '.':
            horz_word_list[counter-1] = '{0}.'.format(horz_word_list[counter-1])
    
    horz_words = ''
    for horz_word in horz_word_list:
        horz_words = "{0}{1};".format(horz_words,horz_word)
    
    print(horz_words)
                
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
        import_alpha_list();
        
    return