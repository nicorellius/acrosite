"""
file        :   build_constructions.py
date        :   2015-01-18
module      :   generator
classes     :
description :   Build constructions for generating acrostics
"""

import random
import operator
import functools

from .parts_of_speech import adj_to_noun_verb_adv, adj_to_noun
from .parts_of_speech import adj_adj_noun_pattern, all_nouns, adj_noun_verb_adv_conn_pattern

from .build_filter import add_first_letter_filter, add_part_of_speech_filter, add_tag_filter
from .build_filter import add_tag_list_filter, condense_tags_list
from .build_filter import add_tag_or_filter, add_list_pos_or_filter, add_pos_to_tags_dictionary_filter
from. build_filter import len_valid_words, len_valid_characters, clean_word, nth_previous_valid_word

from .models import Word

from .generic_constructions import E_A_NP_VP_D_C_pattern, E_A_NP1_VP_NP2_D_C_pattern

def create_word_filter(vert_word, word_list, theme_name, construction_type):
    word_filter = []
    
    if theme_name == 'my_name':
        '''
        [1,2] have equal priority. 3 and 4 are hidden types, which are
        realized when 1 or 2 is selected, and then there is 1/3 chance that
        1 or 2 will be converted to 3 or 4.  1 and 3 are the same (except positive)
        2 and 4are the same (except negative).
        '''
        if construction_type == 1:
            word_filter = my_name_adjectives(vert_word, word_list, True)
        elif construction_type == 2:
            word_filter = my_name_adv_adj(vert_word, word_list, True)
        elif construction_type == 3:
            word_filter = my_name_adjectives(vert_word, word_list, False)
        elif construction_type == 4:
            word_filter = my_name_adv_adj(vert_word, word_list, False)

    elif theme_name == 'cute_animals':
        if construction_type is 1:
            word_filter = cute_animals_verbs(vert_word, word_list)
        else:
            word_filter = cute_animals_theme(vert_word, word_list, construction_type)

    elif theme_name == 'music':
        if construction_type == 1:
            word_filter = instruments_making_music(vert_word, word_list)
        elif construction_type == 2:
            word_filter = animals_jamming(vert_word, word_list)
        elif construction_type == 3:
            word_filter = just_instruments(vert_word, word_list)
            
    return word_filter


def my_name_adjectives(vert_word, word_list, is_positive):
    
    part_of_speech = 'A'

    if is_positive:
        tags = ['positive']
    else:
        tags = ['negative']    
       
    tags.append('to_person')
      
    characters = list(vert_word)
    word_num = len(word_list)

    filters = []
    add_first_letter_filter(filters, characters[word_num])
    add_part_of_speech_filter(filters, part_of_speech)
    add_tag_list_filter(filters, tags)

    return functools.reduce(operator.and_, filters)


def my_name_adv_adj(vert_word, word_list, is_positive):

    characters = list(vert_word)
    word_length = len_valid_characters(characters)
    word_num = len_valid_words(word_list)
    
    part_of_speech = ''

    if is_positive:
        tags = ['positive']

    else:
        tags = ['negative']
    
    if word_length % 2 == 0:
        if word_num % 2 == 0:
            part_of_speech = 'D'
        else:
            part_of_speech = 'A'
    else:
        if word_length - word_num > 3:
            if word_num % 2 == 0:
                part_of_speech = 'D'
            else:
                part_of_speech = 'A'
        else:
            if word_num >= word_length-1:
                part_of_speech = 'A'
            else:
                part_of_speech = 'D'
    
    if part_of_speech == 'A':
        tags.append('to_person')

    elif part_of_speech == 'D':
        tags.append('precede_adjective')
                
    filters = []
    
    add_first_letter_filter(filters, characters[len(word_list)])
    add_tag_list_filter(filters, tags)
    add_part_of_speech_filter(filters, part_of_speech)
    
    return functools.reduce(operator.and_, filters)


def cute_animals_theme(vert_word, word_list, construction_type):
    
    # retrieve original constructions
    if construction_type == 1:
        parts_of_speech = adj_noun_verb_adv_conn_pattern(clean_word(vert_word))
    elif construction_type == 2:
        parts_of_speech = adj_adj_noun_pattern(clean_word(vert_word), True)
    elif construction_type == 3:
        parts_of_speech = adj_to_noun_verb_adv(clean_word(vert_word), True)
    elif construction_type == 4:
        parts_of_speech = adj_to_noun(clean_word(vert_word), True)
    elif construction_type == 5:
        parts_of_speech = all_nouns(clean_word(vert_word), True)

    characters = list(vert_word)
    word_num = len_valid_words(word_list)
       
    filters = []

    add_first_letter_filter(filters, characters[len(word_list)])
    tags = []

    if word_num < len(parts_of_speech):

        add_part_of_speech_filter(filters, parts_of_speech[word_num])
    
        tags = []

        if parts_of_speech[word_num] == 'E':
            tags.append('positive')
        elif parts_of_speech[word_num] == 'A':
            tags.append('positive')
            tags.append('cute_animal_theme')
        elif parts_of_speech[word_num] == 'NP':
            tags.append('cute_animal')
        elif parts_of_speech[word_num] == 'VP':
            tags.append('cute_animal_theme')
        elif parts_of_speech[word_num] == 'D':
            tags.append('follow_verb')
            tags.append('cute_animal_theme')

        add_tag_list_filter(filters, tags)     
    
    return functools.reduce(operator.and_, filters)

def cute_animals_verbs(vert_word, word_list):
    
    pos_tags_master = {
        'E':[],
        'A':['cute_animal_theme','positive'],
        'NP':['cute_animal'],
        'VP':['cute_animal_theme','positive'],
        'D':['follow_verb','positive'],
        'C':[],
    }
    
    return E_A_NP_VP_D_C_pattern(pos_tags_master,vert_word, word_list)


def animals_jamming(vert_word, word_list):
    
    pos_tags_master = {
        'E':[],
        'A':['positive','cute_animal_theme'],
        'NP1':['cute_animal'],
        'VP':['operate_musical_instrument'],
        'NP2':['musical_instrument'],
        'D':['follow_verb','positive'],
        'C':[],
    }
    
    return E_A_NP1_VP_NP2_D_C_pattern(pos_tags_master, vert_word, word_list)

def just_instruments(vert_word, word_list):
    
    filters = []
    part_of_speech = 'NP'
    tags = ['musical_instrument']
    
    characters = list(vert_word)
    
    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, part_of_speech)
    add_tag_list_filter(filters, tags)
    
    return functools.reduce(operator.and_, filters)


def instruments_making_music(vert_word, word_list):
    
    pos_tags_master = {
        'E':[],
        'A':['positive', 'to_person'],
        'NP':['musical_instrument'],
        'VP':['produce_music'],
        'D':['follow_verb','positive'],
        'C':[],
    }
    
    return E_A_NP_VP_D_C_pattern(pos_tags_master,vert_word, word_list)
