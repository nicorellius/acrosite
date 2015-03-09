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
from .build_construction import create_word_filter


logger = logging.getLogger(__name__)


def generate_random_acrostic(vert_word, theme_name):
    
    # database rebuilding: for use with database file import testing
    # rebuild_database(True)
    # rebuild_database(False)
    
    # master list of available options, with weights
    construction_dictionary = {
        'my_name': {1: 4, 2: 3, 3: 2, 4: 1},
        'cute_animals': {1: 5, 2: 2, 3: 1, 4: 1, 5: 1},
        'music': {1: 7, 2: 2, 3: 1},
        }

    # in case the user does not select a theme
    if theme_name not in construction_dictionary:
        theme_name = random.choice(list(construction_dictionary.keys()))
    
    construction_ids_w_weights = construction_dictionary[theme_name]
    
    build_or_rebuild_required = True
    
    while build_or_rebuild_required:

        build_or_rebuild_required = False
    
        construction_type = weighted_random_construction(construction_ids_w_weights)

        print('Construction Type: {0}'.format(construction_type))
        logger.info("{0}: Construction Type: {1}".format(get_timestamp(), construction_type))
        
        horz_word_list = []         # contains the actual word objects
        horz_wordtext_list = []     # contains the text to be rendered to the screen
        
        counter = 0
        characters = list(vert_word)
        
        # for filter_set in filter_sets:
        while counter < len(characters):
        
            word_filter = create_word_filter(vert_word, horz_word_list, theme_name, construction_type)

            # handle duplicates - disallow duplicates unless the entire filtered list has been exhausted
            available_words = list(Word.objects.all().filter(word_filter))
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
                    
                    #TODO: consider re-factor how to handle special characters
                    if characters[counter] is '_':
                        horz_wordtext_list.append('-')
                    else:
                        horz_wordtext_list.append(characters[counter])
                    
                elif len(construction_ids_w_weights) == 1:

                    # No more valid constructions are available.
                    # just return the characters, and a 'None' word.
                    horz_word_list.append(None)
                    horz_wordtext_list.append(characters[counter])
                    
                else:
                    
                    # schedule a rebuild
                    build_or_rebuild_required = True
                    
                    # remove this construction type from the dictionary
                    del(construction_ids_w_weights[construction_type])
                    break

            # select a word at random
            else:
                w = random.choice(duplicate_filtered)
                horz_word_list.append(w)
                horz_wordtext_list.append(re.sub('[_]', ' ', w.name))

            counter += 1
    
    # adjust punctuation accordingly
    horz_wordtext_list = punctuation_modifications(horz_word_list, horz_wordtext_list)
    
    # retrieve other relevant acrostic data, for storage
    parts_of_speech_and_tags = get_pos_and_tags(horz_word_list)
    parts_of_speech = parts_of_speech_and_tags[0]
    tags_list = parts_of_speech_and_tags[1]
        
    horz_words = ''

    for horz_word in horz_wordtext_list:
        horz_words = "{0}{1};".format(horz_words, horz_word)

    logger.info("{0}: Calling `get_or_create()`...".format(get_timestamp()))

    acrostic, created = Acrostic.objects.get_or_create(
        vertical_word=vert_word,
        horizontal_words=horz_words,
        theme_name=theme_name,
        construction_sequence=parts_of_speech,
        tag_sequence=tags_list
    )

    logger.info("{0}: Created new acrostic: {1}".format(get_timestamp(), created))

    level_acrostic = re.sub(';', ' ', acrostic.horizontal_words)

    logger.info("{0}: Acrostic created with vertical word: '{1}'".format(get_timestamp(), vert_word))
    logger.info("{0}: Acrostic:    {1}".format(get_timestamp(), level_acrostic))
    
    return acrostic

def get_pos_and_tags(word_list):
    
    parts_of_speech = []
    tags_list = []
    
    for word in word_list:
        if word is not None:
            parts_of_speech.append(word.part_of_speech)
            tags_list.append(word.tags)
    
    return [parts_of_speech, tags_list]

def weighted_random_construction(construction_ids_w_weights):
        
    construction_id_list = []
    for construction_id in construction_ids_w_weights:
        weight = construction_ids_w_weights[construction_id]
        counter = 0
        while counter < weight:
            construction_id_list.append(construction_id)
            counter += 1
    
    return random.choice(construction_id_list)


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
        logger.info("{0}: Rebuilding entire database...".format(get_timestamp()))
        import_alpha_list()
        logger.info("{0}: Database rebuild complete.".format(get_timestamp()))
        
    return
