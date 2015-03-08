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
from. build_filter import len_valid_words, len_valid_characters, clean_word, nth_previous_valid_word

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
            acrostic_data = animals_jamming_to_pattern(vert_word, word_list)
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


def E_A_NP_VP_D_C_pattern(pos_tags_master, vert_word, word_list):
# a general purpose theme-independent construction that allows
# plugging in a mapping of tags to parts of speech
# used by:
# (1) cute animals
# (2) instruments making music
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
    
    In this case, there are two NPs - NP1 and NP2.
    
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
        
    # dictionary is used often, so initialize here
    A_NP_dict = {
        'A': pos_tags_master['A'],
        'NP': pos_tags_master['NP'],
    }
        
    # first word - can be noun, adjective, or exclamation (if long enough)
    if word_num == 0:
        
        pos_tags_dictionary = {
        'NP': pos_tags_master['NP1'],
        }
        if num_words_remaining > 3:
            pos_tags_dictionary['A'] = pos_tags_master['A']
        if num_words_remaining > 4:
            pos_tags_dictionary['E'] = pos_tags_master['E']
        
        #cannot start with noun in certain cases
        if num_words_remaining == 5 or num_words_remaining == 6:
            pos_tags_dictionary = {
            'A': pos_tags_master['A'],
            'E': pos_tags_master['E'],
            }  
        
        #So that 7-letter words don't contain 4 adjectives in a row
        if num_words_remaining is 7:
            pos_tags_dictionary = {
            'NP': pos_tags_master['NP1'],
            'E': pos_tags_master['E'],
            }
        
        add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
        
    elif nth_previous_valid_word(word_list, 1) is not None:
        
        last_word = nth_previous_valid_word(word_list,1)
        last_pos = last_word.part_of_speech
        last_tags = last_word.tags.split(';')
        last_tags.remove('\n')
        
        # last = NP -> VP
        if last_pos == 'NP':
            add_part_of_speech_filter(filters, 'VP')
            add_tag_list_filter(filters, pos_tags_master['VP'])
        
        # last = VP -> D or C
        elif last_pos == 'VP':
            pos_tags_dictionary = {
            'D': pos_tags_master['D'],
            'C': pos_tags_master['C'],
            }
            
            #last word must be D
            if num_words_remaining == 1:
                add_part_of_speech_filter(filters, 'D')
                add_tag_list_filter(filters, pos_tags_master['D'])
            
            # no choice but to enter a C-NP1-VP-NP2 cycle.
            elif num_words_remaining == 4:
                add_part_of_speech_filter(filters, 'C')
                add_tag_list_filter(filters, pos_tags_master['C'])
                
            # could be either
            else:
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
        
        # last = D -> C
        elif last_pos == 'D':
            add_part_of_speech_filter(filters, 'C')
            add_tag_list_filter(filters, pos_tags_master['C'])
        
        # last = E -> A or NP
        elif last_pos == 'E':
            
            if num_words_remaining == 3 or num_words_remaining == 7:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_list_filter(filters, pos_tags_master['NP'])
            elif num_words_remaining == 4:
                add_pos_to_tags_dictionary_filter(filters, A_NP_dict)
            elif num_words_remaining == 5 or num_words_remaining == 6:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, pos_tags_master['A'])
            
            # more than 7 words remaining
            else:
                add_pos_to_tags_dictionary_filter(filters, A_NP_dict)
                        
        # last = A -> A or NP
        elif last_pos == 'A':
            
            if num_words_remaining == 3 or num_words_remaining == 7:
                add_part_of_speech_filter(filters,'NP')
                add_tag_list_filter(filters,pos_tags_master['NP'])
            elif num_words_remaining == 4:
                
                # prevents a run of 3 adjectives in a row for short vert_words (up to 9 letters).
                use_dict = True
                if word_num >= 2:
                    if (nth_previous_valid_word(word_list, 1).part_of_speech == 'A' 
                        and nth_previous_valid_word(word_list, 2).part_of_speech == 'A'):
                        use_dict = False
                
                if use_dict:
                    add_pos_to_tags_dictionary_filter(filters, A_NP_dict)
                else:
                    add_part_of_speech_filter(filters,'NP')
                    add_tag_list_filter(filters,pos_tags_master['NP'])
                    
            elif num_words_remaining == 5 or num_words_remaining == 6:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, pos_tags_master['A'])
            else:
                add_pos_to_tags_dictionary_filter(filters, A_NP_dict)
                   
        # last = C -> NP or A
        elif last_pos == 'C':
            
            # NP1-D-NP2 cycle
            if num_words_remaining == 3:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_list_filter(filters, pos_tags_master['NP'])
            
            # NP1-VP-NP2-D or A-NP1-VP-NP2
            elif num_words_remaining == 4:
                add_pos_to_tags_dictionary_filter(filters, A_NP_dict)
            
            # 5: A-NP1-VP-NP2-D or A-A-NP1-VP-NP2
            # 6: A-A-NP1-VP-NP-NP2-D (A-A-A-NP1-VP-NP2 is explicitly prevented elsewhere)
            elif num_words_remaining == 5 or num_words_remaining == 6:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, pos_tags_master['A'])

            #to avoid to many adjectives, enter NP1-VP-NP2-C-NP1-VP-NP2
            elif num_words_remaining == 7:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_list_filter(filters, pos_tags_master['NP'])
            
            # more than 7
            else:
                add_pos_to_tags_dictionary_filter(filters, A_NP_dict)

    return [filters, part_of_speech, tags]  


# TODO- refactor the construction into a general place to make this easier.
def animals_jamming_to_pattern(vert_word, word_list):
    
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



def E_A_NP1_VP_NP2_D_C_pattern(pos_tags_master, vert_word, word_list):    
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
    
    In this case, there are two NPs - NP1 and NP2.
    
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
        
    # dictionary is used often, so initialize here
    A_NP1_dict = {
        'A': pos_tags_master['A'],
        'NP': pos_tags_master['NP1'],
    }
        
    # first word - can be noun, adjective, or exclamation (if long enough)
    if word_num == 0:
        
        pos_tags_dictionary = {
        'NP': pos_tags_master['NP1'],
        }
        if num_words_remaining > 3:
            pos_tags_dictionary['A'] = pos_tags_master['A']
        if num_words_remaining > 4:
            pos_tags_dictionary['E'] = pos_tags_master['E']
        
        #cannot start with noun in certain cases
        if num_words_remaining == 5 or num_words_remaining == 6:
            pos_tags_dictionary = {
            'A': pos_tags_master['A'],
            'E': pos_tags_master['E'],
            }  
        
        #So that 7-letter words don't contain 4 adjectives in a row
        if num_words_remaining is 7:
            pos_tags_dictionary = {
            'NP': pos_tags_master['NP1'],
            'E': pos_tags_master['E'],
            }
        
        add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
        
    elif nth_previous_valid_word(word_list, 1) is not None:
        
        last_word = nth_previous_valid_word(word_list,1)
        last_pos = last_word.part_of_speech
        last_tags = last_word.tags.split(';')
        last_tags.remove('\n')
        
        set_last_tags = set(last_tags)
        
        # last = NP1 -> VP
        if last_pos == 'NP' and set(pos_tags_master['NP1']).issubset(set_last_tags):
            add_part_of_speech_filter(filters, 'VP')
            add_tag_list_filter(filters, pos_tags_master['VP'])
        
        # last = VP -> NP2
        elif last_pos == 'VP':
            add_part_of_speech_filter(filters, 'NP')
            add_tag_list_filter(filters, pos_tags_master['NP2'])
        
        # last = D -> C
        elif last_pos == 'D':
            add_part_of_speech_filter(filters, 'C')
            add_tag_list_filter(filters, pos_tags_master['C'])
        
        # last = E -> A or NP1
        elif last_pos == 'E':
            
            if num_words_remaining == 3 or num_words_remaining == 7:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_list_filter(filters, pos_tags_master['NP1'])
            elif num_words_remaining == 4:
                add_pos_to_tags_dictionary_filter(filters, A_NP1_dict)
            elif num_words_remaining == 5 or num_words_remaining == 6:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, pos_tags_master['A'])
            
            # more than 7 words remaining
            else:
                add_pos_to_tags_dictionary_filter(filters, A_NP1_dict)
                        
        # last = A -> A or NP1
        elif last_pos == 'A':
            
            if num_words_remaining == 3 or num_words_remaining == 7:
                add_part_of_speech_filter(filters,'NP')
                add_tag_list_filter(filters,pos_tags_master['NP1'])
            elif num_words_remaining == 4:
                
                # prevents a run of 3 adjectives in a row for short vert_words (up to 9 letters).
                use_dict = True
                if word_num >= 2:
                    if (nth_previous_valid_word(word_list, 1).part_of_speech == 'A' 
                        and nth_previous_valid_word(word_list, 2).part_of_speech == 'A'):
                        use_dict = False
                
                if use_dict:
                    add_pos_to_tags_dictionary_filter(filters, A_NP1_dict)
                else:
                    add_part_of_speech_filter(filters,'NP')
                    add_tag_list_filter(filters,pos_tags_master['NP1'])
                    
            elif num_words_remaining == 5 or num_words_remaining == 6:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, pos_tags_master['A'])
            else:
                add_pos_to_tags_dictionary_filter(filters, A_NP1_dict)
                   
        # last = NP2 -> D or C
        elif last_pos == 'NP' and set(pos_tags_master['NP2']).issubset(set_last_tags):
            pos_tags_dictionary = {
            'D': pos_tags_master['D'],
            'C': pos_tags_master['C'],
            }
            
            #last word must be D
            if num_words_remaining == 1:
                add_part_of_speech_filter(filters, 'D')
                add_tag_list_filter(filters, pos_tags_master['D'])
            
            # no choice but to enter a C-NP1-VP-NP2 cycle.
            elif num_words_remaining == 4:
                add_part_of_speech_filter(filters, 'C')
                add_tag_list_filter(filters, pos_tags_master['C'])
                
            # could be either
            else:
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
        
        # last = C -> NP1 or A
        elif last_pos == 'C':
            
            # NP1-VP-NP2 cycle
            if num_words_remaining == 3:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_list_filter(filters, pos_tags_master['NP1'])
            
            # NP1-VP-NP2-D or A-NP1-VP-NP2
            elif num_words_remaining == 4:
                add_pos_to_tags_dictionary_filter(filters, A_NP1_dict)
            
            # 5: A-NP1-VP-NP2-D or A-A-NP1-VP-NP2
            # 6: A-A-NP1-VP-NP-NP2-D (A-A-A-NP1-VP-NP2 is explicitly prevented elsewhere)
            elif num_words_remaining == 5 or num_words_remaining == 6:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, pos_tags_master['A'])

            #to avoid to many adjectives, enter NP1-VP-NP2-C-NP1-VP-NP2
            elif num_words_remaining == 7:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_list_filter(filters, pos_tags_master['NP1'])
            
            # more than 7
            else:
                add_pos_to_tags_dictionary_filter(filters, A_NP1_dict)

    return [filters, part_of_speech, tags]  

def animals_jamming(vert_word, word_list):
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
         
        # add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)   
        
        #So that 7-letter words don't contain 4 adjectives in a row
        if num_words_remaining is 7:
            pos_tags_dictionary = {
            'NP': ['cute_animal'],
            'E': []
            }
        
        add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
        
    elif nth_previous_valid_word(word_list, 1) is not None:
        
        last_word = nth_previous_valid_word(word_list,1)
        last_pos = last_word.part_of_speech
        last_tags = last_word.tags.split(';')
        
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
                
                # prevents a run of 3 adjectives in a row for short vert_words (up to about 9 letters).
                if word_num >= 2:
                    if (nth_previous_valid_word(word_list, 1).part_of_speech == 'A' 
                        and nth_previous_valid_word(word_list, 2).part_of_speech == 'A'):
                        del pos_tags_dictionary['A']
                        
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
            elif num_words_remaining == 5 or num_words_remaining == 6:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, ['positive', 'cute_animal_theme'])
            elif num_words_remaining == 7:
                add_part_of_speech_filter(filters,'NP')
                add_tag_filter(filters,'cute_animal')
            else:
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
                   
        # last = musical instrument - adverb or connecting expression
        if last_pos == 'NP' and 'musical_instrument' in last_tags:
            pos_tags_dictionary = {
            'D': ['follow_verb','positive'],
            'C': [],
            }
            
            #last word must be an adverb
            if num_words_remaining == 1:
                add_part_of_speech_filter(filters, 'D')
                add_tag_list_filter(filters, ['follow_verb', 'positive'])
            
            # no choice but to enter a connecting expression-cute_animal-play_music-instrument cycle.
            elif num_words_remaining == 4:
                add_part_of_speech_filter(filters, 'C')
                
            # could be either
            else:
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
        
        # last = connecting expression -> cute animal or adjective
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
                add_tag_filter(filters, 'cute_animal')
            
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



# TODO

def flexible_instruments_making_music(vert_word, word_list):
    filters = []
    part_of_speech = ''
    tags = []
    
    characters = list(vert_word)
    word_length = len_valid_characters(characters)
    word_num = len_valid_words(word_list)
    num_words_remaining = word_length - word_num
    
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