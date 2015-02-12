'''
Created on Jan 25, 2015

@author: phillipseitzer
'''
from django.db.models import Q

def add_first_letter_filter(filters, letter):
    filters.append(Q(name__startswith=letter),)
    return filters

def add_word_length_filter(filters, min_length, max_length):
    if min_length:
        filters.append(Q(word_length__lte = max_length))
        
    if max_length:    
        filters.append(Q(word_length__gte = min_length))
    
    return filters

def add_tag_filter(filters, tag):
    filters.append(Q(tags__contains=tag),)
    return filters

def add_tag_list_filter(filters, tag_list):
    for tag in tag_list:
        add_tag_filter(filters, tag)
    return filters

def add_part_of_speech_filter(filters, pos):
    filters.append(Q(part_of_speech=pos),)
    return filters

def add_pos_OR_filter(filters, pos1, pos2):
    filters.append((Q(part_of_speech=pos1) | Q(part_of_speech=pos2)))
    return filters

def add_tag_OR_filter(filters, tag1, tag2):
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
            ['A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']):
            valid_char_list.append(1)
        else:
            valid_char_list.append(0)
            
    return valid_char_list

def len_valid_characters(vert_word):
    
    characters = list(vert_word)
    counter = 0
    for character in characters:
        if (character.upper() in 
            ['A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']):
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
    counter = 0;
    valid_chars = [];
    for character in characters:
        if (character.upper() in 
            ['A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']):
            valid_chars.append(character)
            counter += 1
    
    cleaned_word = ''.join(str(x) for x in valid_chars)
    return cleaned_word

#TODO: currently unusued, but may be useful in future?
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

    print('VALID CHAR:{0}'.format(characters[any_char_number-1]))
    return characters[any_char_number-1]
    
    
    