"""
file        :   build_filter.py
date        :   2015-03-10
module      :   themes
classes     :
description :   Utility methods used in creating a filter out of a word list.
"""

import logging

from django.db.models import Q
import operator
import functools

from common.util import get_timestamp


logger = logging.getLogger(__name__)

timestamp = get_timestamp()


def add_first_letter_filter(filters, letter):
    filters.append(Q(name__startswith=letter),)

    return filters


def add_tag_filter(filters, tag):
    filters.append(Q(tags__contains=tag),)

    return filters


def add_tag_list_filter(filters, tag_list):
    
    if tag_list is not []:
        for tag in tag_list:
            add_tag_filter(filters, tag)

    return filters


def add_part_of_speech_filter(filters, pos):
    filters.append(Q(part_of_speech=pos),)

    return filters

def add_list_pos_or_filter(filters, list_pos):
    or_filters = []
    for pos in list_pos:
        or_filters.append(Q(part_of_speech=pos))
    
    filters.append(functools.reduce(operator.or_, or_filters))
    return filters

def add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary):
    combined_filter = []
    for pos, list_tags in pos_tags_dictionary.items():
        entry_filter = []
        entry_filter.append(Q(part_of_speech=pos))
        for tag in list_tags:
            entry_filter.append(Q(tags__contains=tag))
        combined_filter.append(functools.reduce(operator.and_, entry_filter))
        
    filters.append(functools.reduce(operator.or_, combined_filter))
    return filters
    
def add_tag_or_filter(filters, tag1, tag2):
    filters.append((Q(tags__contains=tag1) | Q(tags__contains=tag2)))

    return filters


def condense_tags_list(tag_list_list):
    formatted_tag_list = []

    for tag_list in tag_list_list:
        formatted_tag_list.append(";".join(tag_list))
    
    return formatted_tag_list


def get_valid_chars(vert_word):
    
    characters = list(vert_word)
    valid_char_list = []
    
    for character in characters:

        if (character.upper() in
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']):

            valid_char_list.append(1)

        else:
            valid_char_list.append(0)
            
    return valid_char_list


# get valid length of word
def len_valid_characters(vert_word):
    
    characters = list(vert_word)
    counter = 0

    for character in characters:

        if (character.upper() in
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']):

            counter += 1
    
    return counter


def len_valid_words(word_list):
    
    counter = 0

    for word in word_list:

        if word is not None:
            counter += 1
         
    return counter


def clean_word(vert_word):
    
    characters = list(vert_word)
    counter = 0
    valid_chars = []

    for character in characters:

        if (character.upper() in
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']):

            valid_chars.append(character)

            counter += 1
    
    cleaned_word = ''.join(str(x) for x in valid_chars)

    return cleaned_word

def nth_previous_valid_word(word_list, num_back):
    
    word = None
    num_back = num_back-1
    if num_back < len_valid_words(word_list):
        valid_words_counter = 0
        all_words_counter = len(word_list)
        while (valid_words_counter <= num_back):
            all_words_counter = all_words_counter - 1
            if word_list[all_words_counter] is not None:
                valid_words_counter += 1
                word = word_list[all_words_counter]
     
    # for debugging
    #print('BACK:{0} WORD LIST:{1}'.format((num_back+1), word_list))
    #print('BACK:{0} PREV WORD:{1}'.format((num_back+1), word))           
    return word
# TODO: currently unusued, but may be useful in future?
def valid_char_at(vert_word, desired_valid_char_number):
    
    characters = list(vert_word)
    valid_chars = get_valid_chars(vert_word)
    total_valid = len_valid_characters(vert_word)
    
    if desired_valid_char_number >= total_valid:
        return '?'
    
    any_char_number = 0
    valid_char_number = -1

    while valid_char_number < desired_valid_char_number:
        valid_char_number += valid_chars[any_char_number]
        any_char_number += 1

    print('VALID CHAR:{0}'.format(characters[any_char_number - 1]))
    logger.info("{0}: VALID CHAR:{0}".format(get_timestamp(), characters[any_char_number - 1]))

    return characters[any_char_number - 1]