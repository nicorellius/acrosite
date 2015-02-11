"""
file        :   generate.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   Generate an acrostic based on various inputs and the database of words.
"""

import random
import re
import logging

from common.util import get_timestamp

from .models import Word, Acrostic
from .populate import import_alpha_list
from .build_construction import create_acrostic_filters


logger = logging.getLogger(__name__)

timestamp = get_timestamp()


def generate_random_acrostic(vert_word, theme_name):
    
    # database rebuilding: for use with database file import testing
    # rebuild_database(True)
    # rebuild_database(False)
    
    # master list of available options
    construction_dictionary = {
        'my_name': [[1, 2]],
        'cute_animals': [[1, 2], [3, 4], [5]],
        'music': [[1], [2], [3]],
        }
    
    # in case the user does not select a theme
    if theme_name not in construction_dictionary:
        theme_name = random.choice(list(construction_dictionary.keys()))
    
    construction_preference_level = 0
    construction_id_list = construction_dictionary[theme_name][construction_preference_level]
    
    build_or_rebuild_required = True
    
    while build_or_rebuild_required:
        build_or_rebuild_required = False
    
        construction_type = random.choice(construction_id_list)
        
        # TODO: think about handling this in a more intelligent way
        add_on_value = 0
        if theme_name == 'my_name':
            add_ons = [0,0,0,2]
            add_on_value = random.choice(add_ons)
            construction_type += add_on_value
        
        horz_word_list = []         # contains the actual word objects
        horz_wordtext_list = []     # contains the text to be rendered to the screen
        parts_of_speech = []
        tags_list = []
        
        counter = 0
        characters = list(vert_word)
        
        # for filter_set in filter_sets:
        while counter < len(characters):
        
            acrostic_data = create_acrostic_filters(vert_word, horz_word_list, theme_name, construction_type)
            filter_set = acrostic_data[0]
            parts_of_speech.append(acrostic_data[1])
            tags_list.append(acrostic_data[2])
            
            # initial state- all objects
            pre_filter = Word.objects.all()
        
            # filter based on construction and vertical word
            for filter_query in filter_set:
                post_filter = pre_filter.filter(filter_query)
                pre_filter = post_filter
        
            # handle duplicates - disallow duplicates unless the entire filtered list has been exhausted
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
                
                # check if the character is not a word character - in which case, just ignore
                if (characters[counter].upper() not in
                    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']):
                    
                    # treat strange character as a 'None', return just the character
                    horz_word_list.append(None)
                    horz_wordtext_list.append(characters[counter])
                    
                elif len(construction_id_list) == 1:  # no more constructions in this preference level
                    if (construction_preference_level+1) < len(construction_dictionary[theme_name]):
                        # move to the next preference level
                        build_or_rebuild_required = True
                        construction_preference_level += 1
                        construction_id_list = construction_dictionary[theme_name][construction_preference_level]
                        break
                    else:
                        # no more preference levels, and no more constructions in this preference level.
                        # just return the characters, and a 'None' word.
                        horz_word_list.append(None)
                        horz_wordtext_list.append(characters[counter])
                else:
                    # check other constructions in this level
                    build_or_rebuild_required = True
                    construction_id_list.remove(construction_type-add_on_value)
                    break

            # select a word at random
            else:
                w = random.choice(duplicate_filtered)
                horz_word_list.append(w)
                horz_wordtext_list.append(re.sub('[_]', ' ', w.name))

            counter += 1
    
    horz_wordtext_list = punctuation_modifications(horz_word_list, horz_wordtext_list)
    
    horz_words = ''
    for horz_word in horz_wordtext_list:
        horz_words = "{0}{1};".format(horz_words, horz_word)

    logger.info("{0}: calling get_or_create()...".format(get_timestamp()))

    acrostic, created = Acrostic.objects.get_or_create(
        vertical_word=vert_word,
        horizontal_words=horz_words,
        theme_name=theme_name,
        construction_sequence=parts_of_speech,
        tag_sequence=tags_list
    )

    level_acrostic = re.sub(';', ' ', acrostic.horizontal_words)

    logger.info("{0}: acrostic created with vertical word: '{1}'".format(timestamp, vert_word))
    logger.info("{0}: acrostic:    {1}".format(timestamp, level_acrostic))
    
    return acrostic


def punctuation_modifications(horz_word_list, horz_wordtext_list):
    
    counter = 1
    period_to_last = False
    while counter < len(horz_wordtext_list):
        chars = list(horz_wordtext_list[counter])
        if chars[len(chars) - 1] == ',':
            actual_word = counter - 1
            while horz_word_list[actual_word] is None:
                actual_word -= 1
            horz_wordtext_list[actual_word] = '{0}.'.format(horz_wordtext_list[actual_word])
            period_to_last = True
        counter += 1

    if period_to_last:
        actual_word = counter - 1
        while horz_word_list[actual_word] is None:
            actual_word -= 1
        if horz_wordtext_list[actual_word] != '.':
            horz_wordtext_list[actual_word] = '{0}.'.format(horz_wordtext_list[actual_word])

    return horz_wordtext_list


def rebuild_database(force_rebuild):
    
    if force_rebuild is True:
        Word.objects.all().delete()
    
    if not Word.objects.all():
        print("Rebuilding entire database...")
        import_alpha_list()
        
    return
