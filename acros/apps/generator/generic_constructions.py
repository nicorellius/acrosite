'''
Created on Mar 8, 2015

@author: phillipseitzer
'''

import functools
import operator

from .build_filter import add_first_letter_filter, add_part_of_speech_filter
from .build_filter import add_tag_list_filter
from .build_filter import add_pos_to_tags_dictionary_filter
from .build_filter import len_valid_words, len_valid_characters, nth_previous_valid_word

def all_same(pos, tags, vert_word, word_list):
    
    characters = list(vert_word)
    
    filters = []
    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, pos)
    add_tag_list_filter(filters, tags)
    
    return functools.reduce(operator.and_, filters)


def pos1_pos2(pos1, pos2, pos_tags_master, vert_word, word_list):
    
    characters = list(vert_word)
    word_length = len_valid_characters(characters)
    word_num = len_valid_words(word_list)
    
    part_of_speech = ''
    
    if word_length % 2 == 0:
        if word_num % 2 == 0:
            part_of_speech = pos1
        else:
            part_of_speech = pos2
    else:
        if word_length - word_num > 3:
            if word_num % 2 == 0:
                part_of_speech = pos1
            else:
                part_of_speech = pos2
        else:
            if word_num >= word_length-1:
                part_of_speech = pos2
            else:
                part_of_speech = pos1
                
    filters = []
    
    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, part_of_speech)
    add_tag_list_filter(filters, pos_tags_master[part_of_speech])
    
    return functools.reduce(operator.and_, filters)


def E_A_NP_VP_D_C_pattern(pos_tags_master, vert_word, word_list):

    filters = []
    
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
        'NP': pos_tags_master['NP'],
        }
        if num_words_remaining >= 3:
            pos_tags_dictionary['A'] = pos_tags_master['A']
            pos_tags_dictionary['E'] = pos_tags_master['E']
        
        #cannot start with noun in certain cases
        if num_words_remaining == 4:
            pos_tags_dictionary = {
            'A': pos_tags_master['A'],
            'E': pos_tags_master['E'],
            }
        
        add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
        
    elif nth_previous_valid_word(word_list, 1) is not None:
        
        last_word = nth_previous_valid_word(word_list,1)
        last_pos = last_word.part_of_speech
        last_tags = last_word.tags.split(';')
        if '\n' in last_tags:
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
            
            #must proceed as D
            if num_words_remaining == 1:
                add_part_of_speech_filter(filters, 'D')
                add_tag_list_filter(filters, pos_tags_master['D'])
            # must proceed as C-NP-VP
            elif num_words_remaining == 3:
                add_part_of_speech_filter(filters, 'C')
                add_tag_list_filter(filters, pos_tags_master['C'])
            else:
                add_pos_to_tags_dictionary_filter(filters, pos_tags_dictionary)
        
        # last = D -> C
        elif last_pos == 'D':
            add_part_of_speech_filter(filters, 'C')
            add_tag_list_filter(filters, pos_tags_master['C'])
        
        # last = E -> A or NP
        elif last_pos == 'E':
            
            # must proceed as NP-VP
            if num_words_remaining == 2:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_list_filter(filters, pos_tags_master['NP'])
            # must proceed as A-NP-VP-D
            elif num_words_remaining == 4:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, pos_tags_master['A'])
            else:
                add_pos_to_tags_dictionary_filter(filters, A_NP_dict)
                        
        # last = A -> A or NP
        elif last_pos == 'A':
            
            # must proceed as NP-VP
            if num_words_remaining == 2:
                add_part_of_speech_filter(filters,'NP')
                add_tag_list_filter(filters,pos_tags_master['NP'])
            elif num_words_remaining == 3:
                
                # prevents a run of 3 adjectives in a row.
                use_dict = True
                if word_num >= 2:
                    if nth_previous_valid_word(word_list, 2).part_of_speech == 'A':
                        use_dict = False
                
                if use_dict:
                    add_pos_to_tags_dictionary_filter(filters, A_NP_dict)
                else:
                    add_part_of_speech_filter(filters,'NP')
                    add_tag_list_filter(filters,pos_tags_master['NP'])
            
            # must proceed as A-NP-VP-D
            elif num_words_remaining == 4:
                add_part_of_speech_filter(filters,'A')
                add_tag_list_filter(filters,pos_tags_master['A'])
            # must proceed as NP-VP-C-NP-VP
            elif num_words_remaining == 5:
                add_part_of_speech_filter(filters,'NP')
                add_tag_list_filter(filters,pos_tags_master['NP'])
            else:
                add_pos_to_tags_dictionary_filter(filters, A_NP_dict)
                   
        # last = C -> NP or A
        elif last_pos == 'C':
            
            # must proceed as NP-VP
            if num_words_remaining == 2 or num_words_remaining == 5:
                add_part_of_speech_filter(filters, 'NP')
                add_tag_list_filter(filters, pos_tags_master['NP'])
            # must proceed as A-NP-VP-D
            elif num_words_remaining == 4:
                add_part_of_speech_filter(filters, 'A')
                add_tag_list_filter(filters, pos_tags_master['A'])
            else:
                add_pos_to_tags_dictionary_filter(filters, A_NP_dict)


    return functools.reduce(operator.and_, filters) 


def E_A_NP1_VP_NP2_D_C_pattern(pos_tags_master, vert_word, word_list):    

    filters = []

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
        if '\n' in last_tags:
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
                
                # TODO: last pos is already an A, change conditional statement
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
            # 6: A-A-NP1-VP-NP-NP2-D (A-A-A-NP1-VP-NP2 is explicitly prevented by last_pos='A')
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

    return functools.reduce(operator.and_, filters) 