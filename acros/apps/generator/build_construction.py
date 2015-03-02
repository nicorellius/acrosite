"""
file        :   build_constructions.py
date        :   2015-01-18
module      :   generator
classes     :
description :   Build constructions for generating acrostics
"""

import random

from .parts_of_speech import adj_to_noun_verb_adv, adj_to_noun
from .parts_of_speech import adj_adj_noun_pattern, all_nouns, adj_noun_verb_adv_conn_pattern

from .build_filter import add_first_letter_filter, add_part_of_speech_filter, add_tag_filter
from .build_filter import add_tag_list_filter, condense_tags_list
from .build_filter import add_tag_or_filter, add_list_pos_or_filter, add_pos_to_tags_dictionary_filter
from. build_filter import len_valid_words, len_valid_characters, clean_word

from .models import Word


def create_acrostic_filters(vert_word, word_list, theme_name, construction_type):
    acrostic_data = []
    
    if theme_name == 'my_name':
        '''
        [1,2] have equal priority. 3 and 4 are hidden types, which are
        realized when 1 or 2 is selected, and then there is 1/3 chance that
        1 or 2 will be converted to 3 or 4.  1 and 3 are the same (except positive)
        2 and 4are the same (except negative).
        '''
        if construction_type == 1:
            acrostic_data = my_name_adjectives(vert_word, word_list, True)
        elif construction_type == 2:
            acrostic_data = my_name_adv_adj(vert_word, word_list, True)
        elif construction_type == 3:
            acrostic_data = my_name_adjectives(vert_word, word_list, False)
        elif construction_type == 4:
            acrostic_data = my_name_adv_adj(vert_word, word_list, False)

    elif theme_name == 'cute_animals':
        acrostic_data = cute_animals_theme(vert_word, word_list, construction_type)

    elif theme_name == 'music':
        if construction_type == 1:
            acrostic_data = instruments_making_music(vert_word, word_list)
        elif construction_type == 2:
            #acrostic_data = animals_jamming(vert_word, word_list)
            acrostic_data = flexible_animals_jamming(vert_word, word_list)
        elif construction_type == 3:
            acrostic_data = just_instruments(vert_word, word_list)
            
    return acrostic_data


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

    return [filters, part_of_speech, tags]


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
    
    return [filters, part_of_speech, tags]


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

        part_of_speech = parts_of_speech[word_num]
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

    else:
        part_of_speech = ''        
    
    return [filters, part_of_speech, condense_tags_list(tags)]


def animals_jamming(vert_word, word_list):
    
    filters = []
    part_of_speech = ''
    tags = []
    
    characters = list(vert_word)
    word_length = len_valid_characters(characters)
    word_num = len_valid_words(word_list)
    
    if word_length > 10:
        
        parts_of_speech = []
        tags_list = []
        
        if word_length % 4 == 0:
            tags_list.append([])
            parts_of_speech.append('E')
            
        elif word_length % 4 == 1:
            tags_list.append([])
            parts_of_speech.append('E')
            
            tags_list.append(['positive', 'cute_animal_theme'])
            parts_of_speech.append('A')

        elif word_length % 4 == 2:

            tags_list.append([])
            parts_of_speech.append('E')
            
            tags_list.append(['positive', 'cute_animal_theme'])
            parts_of_speech.append('A')
            
            tags_list.append(['positive', 'cute_animal_theme'])
            parts_of_speech.append('A')
            
        counter = 0

        while counter < word_length:
            parts_of_speech.append('NP')
            parts_of_speech.append('VP')
            parts_of_speech.append('NP')
                
            tags_list.append(['cute_animal'])
            tags_list.append(['operate_musical_instrument'])
            tags_list.append(['musical_instrument'])
            
            if counter + 3 < word_length:
                parts_of_speech.append('C')
                tags_list.append([])
            
            counter += 4
         
        part_of_speech = parts_of_speech[word_num]
        tags = tags_list[word_num]

    if word_length == 10:

        if word_num == 0:
            part_of_speech = 'E'
            tags = []
        elif word_num == 1:
            part_of_speech = 'A'
            tags = ['positive', 'cute_animal_theme']
        elif word_num == 2:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 3:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']
        elif word_num == 4:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
        elif word_num == 5:
            part_of_speech = 'C'
            tags = []
        elif word_num == 6:
            part_of_speech = 'A'
            tags = ['cute_animal_theme', 'positive']
        elif word_num == 7:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 8:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']
        elif word_num == 9:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
                
    if word_length == 9:

        if word_num == 0:
            part_of_speech = 'A'
            tags = ['positive', 'cute_animal_theme']
        elif word_num == 1:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 2:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']
        elif word_num == 3:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
        elif word_num == 4:
            part_of_speech = 'C'
            tags = []
        elif word_num == 5:
            part_of_speech = 'A'
            tags = ['cute_animal_theme', 'positive']
        elif word_num == 6:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 7:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']
        elif word_num == 8:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
    
    if word_length == 8:

        if word_num == 0:
            part_of_speech = 'E'
            tags = []
        elif word_num == 1:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 2:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']
        elif word_num == 3:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
        elif word_num == 4:
            part_of_speech = 'C'
            tags = []
        elif word_num == 5:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 6:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']
        elif word_num == 7:
            part_of_speech = 'NP'
            tags = ['musical_instrument']

    if word_length == 7:
        if word_num == 0:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 1:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']
        elif word_num == 2:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
        elif word_num == 3:
            part_of_speech = 'C'
            tags = []
        elif word_num == 4:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 5:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']
        elif word_num == 6:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
    
    # start with exclamation.
    # if word_length > 3 and word_length < 7:
    # simplified this chained comparison
    if 7 > word_length > 3:

        if word_length - word_num == 6:
            part_of_speech = 'E'
            tags = ['positive']
        elif word_length - word_num == 5:
            part_of_speech = 'A'
            tags = ['positive', 'cute_animal_theme']
        elif word_length - word_num == 4:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_length - word_num == 3:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']
        elif word_length - word_num == 2:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
        elif word_length - word_num == 1:
            part_of_speech = 'D'
            tags = ['follow_verb', 'positive']
    
    if word_length == 3:

        if word_num == 0:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 1:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']
        elif word_num == 2:
            part_of_speech = 'NP'
            tags = ['musical_instrument']

    if word_length == 2:

        if word_num == 0:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 1:
            part_of_speech = 'VP'
            tags = ['operate_musical_instrument']

    if word_length == 1:

        part_of_speech = 'NP'
        tags = ['cute_animal']
        
    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, part_of_speech)
    add_tag_list_filter(filters, tags)
    
    return [filters, part_of_speech, tags]

def flexible_animals_jamming(vert_word, word_list):
    '''
    Description:
    ------------
    Rather than hard-code a construct like adjective-verb-adverb,
    this construct allows for more flexible word creation.  Based on
    (1) knowledge of the final length of the word
    and
    (2) the previous words used,
    an acceptable word is chosen.  For example, following a verb, both
    an adverb (modifying the previous verb) or a noun (indicating a new sentence),
    or a connecting expresion (also indicating a new sentence) or an adjective (indicating
    the modifier of a new sentence) might be acceptable.  Depending on what is chosen, however,
    the following word should change.
    '''
    filters = []
    part_of_speech = ''
    tags = []
    
    characters = list(vert_word)
    word_length = len_valid_characters(characters)
    word_num = len_valid_words(word_list)
    num_words_remaining = word_length - word_num
    
    # first letter must always match
    add_first_letter_filter(filters, characters[len(word_list)])
        
    # first word - can be noun, adjective, or exclamation (if long enough)
    if word_num == 0:
        
        pos_tags_dictionary = {
        'NP': ['cute_animal'],
        }
        if num_words_remaining > 3:
            pos_tags_dictionary['A'] = ['positive', 'cute_animal_theme']
        if num_words_remaining > 4:
            pos_tags_dictionary['E'] = []
        
        #cannot start with noun in certain cases
        if num_words_remaining == 5 or num_words_remaining == 6:
            pos_tags_dictionary = {
            'A': ['positive', 'cute_animal_theme'],
            'E': []
            }
         
        add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)   
        
        # TODO - handle this?
        # special case - so that 7-letter words don't contain 4 adjectives
        #if num_words_remaining is 7:
            #add_tag_filter(filters, 'cute_animal')
            #add_part_of_speech_filter(filters, 'NP')
        #else:
        #    add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
        
    else:
        last_word = word_list[word_num-1]
        last_pos = last_word.part_of_speech
        last_tags = last_word.tags.split(';')
        print(last_tags)
        
        # last = cute animal -> verb: operate musical instrument
        if last_pos == 'NP' and 'cute_animal' in last_tags:
            add_part_of_speech_filter(filters, 'VP')
            add_tag_filter(filters, 'operate_musical_instrument')
        
        # last = operate musical instrument -> musical_instrument
        if last_pos == 'VP':
            add_part_of_speech_filter(filters, 'NP')
            add_tag_filter(filters, 'musical_instrument')
        
        # last = adverb -> connexpr
        if last_pos == 'D':
            add_part_of_speech_filter(filters, 'C')
        
        # last = exclamation -> adjective or cute animal
        if last_pos == 'E':
            pos_tags_dictionary = {
            'A': ['positive', 'cute_animal_theme'],
            'NP': ['cute_animal']
            }
            
            if num_words_remaining == 3:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_filter(filters, 'cute_animal')
            elif num_words_remaining == 4:
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
            elif num_words_remaining == 5 or num_words_remaining == 6:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, ['positive', 'cute_animal_theme'])
            elif num_words_remaining == 7:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_filter(filters, 'cute_animal')
            
            # more than 7 words remaining
            else:
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
                        
        # last = adjective -> more adjectives or cute animal
        if last_pos == 'A':
            pos_tags_dictionary = {
            'A': ['positive', 'cute_animal_theme'],
            'NP': ['cute_animal']
            }
            
            if num_words_remaining == 3:
                add_part_of_speech_filter(filters,'NP')
                add_tag_filter(filters,'cute_animal')
            elif num_words_remaining == 4:
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
            elif num_words_remaining == 5 or num_words_remaining == 6:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, ['positive', 'cute_animal_theme'])
            elif num_words_remaining == 7:
                add_part_of_speech_filter(filters,'NP')
                add_tag_filter(filters,'cute_animal')
            else:
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
                   
        # last = musical instrument - adverb or connexpr
        if last_pos == 'NP' and 'musical_instrument' in last_tags:
            pos_tags_dictionary = {
            'D': ['follow_verb','positive'],
            'C': [],
            }
            
            #last word must be an adverb
            if num_words_remaining == 1:
                add_part_of_speech_filter(filters, 'D')
                add_tag_list_filter(filters, ['follow_verb', 'positive'])
            
            # no choice but to enter a connexpr-cute_animal-play_music-instrument cycle.
            elif num_words_remaining == 4:
                add_part_of_speech_filter(filters, 'C')
                
            # could be either
            else:
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
        
        # last = connexpr -> cute animal or adjective
        if last_pos == 'C':
            
            # cute_animal-play_music-instrument cycle
            if num_words_remaining == 3:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_filter(filters, 'cute_animal')
            
            # cute_animal-play_music-instrument-adverb
            # or
            # adjective-cute_animal-play_music-instrument
            elif num_words_remaining == 4:
                pos_tags_dictionary = {
                    'A': ['cute_animal_theme','positive'],
                    'NP': ['cute_animal'],
                }
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
                
            # 5:
            # adjective-cute_animal-plays_music-instrument-adverb
            # or
            # adjective-adjective-cute_animal-plays_music-instrument
            # 
            # 6:
            # adjective-adjective-cute_animal-plays_music-instrument-adverb
            # or
            # adjective-adjective-adjective-cute_animal-plays_music-instrument
            elif num_words_remaining == 5 or num_words_remaining == 6:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, ['positive', 'cute_animal_theme'])

            #force to enter double-construction mode to avoid too many adjectives
            elif num_words_remaining == 7:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_filter('cute_animal')
            
            # more than 7
            else:
                pos_tags_dictionary = {
                    'A': ['cute_animal_theme','positive'],
                    'NP': ['cute_animal'],
                }
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)

                
    
    return [filters, part_of_speech, tags]

def just_instruments(vert_word, word_list):
    
    filters = []
    part_of_speech = 'NP'
    tags = ['musical_instrument']
    
    characters = list(vert_word)
    
    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, part_of_speech)
    add_tag_list_filter(filters, tags)
    
    return [filters, part_of_speech, tags]


def instruments_making_music(vert_word, word_list):
    
    tags = []
    filters = []
    parts_of_speech = []
    
    characters = list(vert_word)
    word_length = len_valid_characters(characters)
    word_num = len_valid_words(word_list)
    
    if word_length == 1:
        parts_of_speech = ['NP']
        tags = [['musical_instrument']]
    elif word_length == 2:
        parts_of_speech = ['NP', 'VP']
        tags = [
            ['musical_instrument'],
            ['produce_music']
        ]
    elif word_length == 3:
        parts_of_speech = ['NP', 'VP', 'D']
        tags = [
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb']
        ]
    elif word_length == 4:
        parts_of_speech = ['A', 'NP', 'VP', 'D']
        tags = [
            ['positive', 'to_person'],
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb']
        ]
    elif word_length == 5:
        parts_of_speech = ['NP', 'VP', 'C', 'NP', 'VP']
        tags = [
            ['musical_instrument'],
            ['produce_music'],
            [],
            ['musical_instrument'],
            ['produce_music']
        ]
    elif word_length == 6:
        parts_of_speech = ['NP', 'VP', 'C', 'NP', 'VP', 'D']
        tags = [
            ['musical_instrument'],
            ['produce_music'],
            [],
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb']
        ]
    elif word_length == 7:
        parts_of_speech = ['NP', 'VP', 'D', 'C', 'NP', 'VP', 'D']
        tags = [
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb'],
            [], ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb']
        ]
    elif word_length == 8:
        parts_of_speech = ['A', 'NP', 'VP', 'D', 'C', 'NP', 'VP', 'D']
        tags = [
            ['to_person', 'positive'],
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb'],
            [],
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb']
        ]
    elif word_length == 9:
        parts_of_speech = ['A', 'NP', 'VP', 'D', 'C', 'A', 'NP', 'VP', 'D']
        tags = [
            ['positive', 'to_person'],
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb'],
            [],
            ['to_person', 'positive'],
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb']
        ]
    elif word_length == 10:
        parts_of_speech = ['A', 'A', 'NP', 'VP', 'D', 'C', 'A', 'NP', 'VP', 'D']
        tags = [
            ['to_person', 'positive'],
            ['to_person', 'positive'],
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb'],
            [],
            ['to_person', 'positive'],
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb']
        ]
    elif word_length == 11:
        parts_of_speech = ['NP', 'VP', 'D', 'C', 'NP', 'VP', 'D', 'C', 'NP', 'VP', 'D']
        tags = [
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb'],
            [],
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb'],
            [],
            ['musical_instrument'],
            ['produce_music'],
            ['positive', 'follow_verb']
        ]
    else:
        if word_length % 4 == 0:
            tags.append(['positive', 'to_person'])
            parts_of_speech.append('A')
            
        elif word_length % 4 == 1:
            tags.append(['positive', 'to_person'])
            parts_of_speech.append('A')
            
            tags.append(['positive', 'to_person'])
            parts_of_speech.append('A')

        elif word_length % 4 == 2:

            tags.append(['positive', 'to_person'])
            parts_of_speech.append('A')
            
            tags.append(['positive', 'to_person'])
            parts_of_speech.append('A')
            
            tags.append(['positive', 'to_person'])
            parts_of_speech.append('A')

        counter = 0

        while counter < word_length:

            parts_of_speech.append('NP')
            parts_of_speech.append('VP')
            parts_of_speech.append('D')
                
            tags.append(['musical_instrument'])
            tags.append(['produce_music'])
            tags.append(['positive', 'follow_verb'])
            
            if counter + 3 < word_length:
                parts_of_speech.append('C')
                tags.append([])
            
            counter += 4

    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, parts_of_speech[word_num])
    add_tag_list_filter(filters, tags[word_num])
    
    return [filters, parts_of_speech[word_num], condense_tags_list(tags[word_num])]