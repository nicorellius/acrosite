'''
Created on Jan 18, 2015

@author: phillipseitzer
'''

import random

from .parts_of_speech import adj_to_noun_verb_adv, adj_to_noun, adj_adj_noun_pattern, all_adj, all_nouns
from .tags import same_except_last

from .build_filter import add_first_letter_filter,add_part_of_speech_filter,add_tag_filter
from .build_filter import add_tag_list_filter,condense_tags_list,add_tag_OR_filter,add_pos_OR_filter
from. build_filter import len_valid_words,len_valid_characters,clean_word

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
            acrostic_data = animals_jamming(vert_word, word_list)
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
        parts_of_speech = adj_to_noun_verb_adv(clean_word(vert_word), True)
    elif construction_type == 2:
        parts_of_speech = adj_to_noun(clean_word(vert_word), True);
    elif construction_type == 3:
        parts_of_speech = adj_adj_noun_pattern(clean_word(vert_word), True);
    elif construction_type == 4:
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
        if parts_of_speech[word_num] == 'A':
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
            
            tags_list.append(['positive','cute_animal_theme'])
            parts_of_speech.append('A')

        elif word_length % 4 == 2:

            tags_list.append([])
            parts_of_speech.append('E')
            
            tags_list.append(['positive','cute_animal_theme'])
            parts_of_speech.append('A')
            
            tags_list.append(['positive','cute_animal_theme'])
            parts_of_speech.append('A')
            
        counter = 0
        while counter < word_length:
            parts_of_speech.append('NP')
            parts_of_speech.append('VP')
            parts_of_speech.append('NP')
                
            tags_list.append(['cute_animal'])
            tags_list.append(['make_music'])
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
            tags = ['positive','cute_animal_theme']
        elif word_num == 2:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 3:
            part_of_speech = 'VP'
            tags = ['make_music']
        elif word_num == 4:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
        elif word_num == 5:
            part_of_speech = 'C'
            tags = []
        elif word_num == 6:
            part_of_speech = 'A'
            tags = ['cute_animal_theme','positive']
        elif word_num == 7:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 8:
            part_of_speech = 'VP'
            tags = ['make_music']
        elif word_num == 9:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
                
    if word_length == 9:
        if word_num == 0:
            part_of_speech = 'A'
            tags = ['positive','cute_animal_theme']
        elif word_num == 1:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 2:
            part_of_speech = 'VP'
            tags = ['make_music']
        elif word_num == 3:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
        elif word_num == 4:
            part_of_speech = 'C'
            tags = []
        elif word_num == 5:
            part_of_speech = 'A'
            tags = ['cute_animal_theme','positive']
        elif word_num == 6:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 7:
            part_of_speech = 'VP'
            tags = ['make_music']
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
            tags = ['make_music']
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
            tags = ['make_music']
        elif word_num == 7:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
    
    
    if word_length == 7:
        if word_num == 0:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 1:
            part_of_speech = 'VP'
            tags = ['make_music']
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
            tags = ['make_music']
        elif word_num == 6:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
    
    # start with exclamation.
    if word_length > 3 and word_length < 7:
        if word_length - word_num  == 6:
            part_of_speech = 'E'
            tags = ['positive']
        elif word_length - word_num == 5:
            part_of_speech = 'A'
            tags = ['positive','cute_animal_theme']
        elif word_length - word_num == 4:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_length - word_num == 3:
            part_of_speech = 'VP'
            tags = ['make_music']
        elif word_length - word_num == 2:
            part_of_speech = 'NP'
            tags = ['musical_instrument']
        elif word_length - word_num == 1:
            part_of_speech = 'D'
            tags = ['follow_verb','positive']
    
    if word_length == 3:
        if word_num == 0:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 1:
            part_of_speech = 'VP'
            tags = ['make_music']
        elif word_num == 2:
            part_of_speech = 'NP'
            tags = ['musical_instrument']

    if word_length == 2:
        if word_num == 0:
            part_of_speech = 'NP'
            tags = ['cute_animal']
        elif word_num == 1:
            part_of_speech = 'VP'
            tags = ['make_music']

    if word_length == 1:
        part_of_speech = 'NP'
        tags = ['cute_animal']
        
    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, part_of_speech)
    add_tag_list_filter(filters, tags)
    
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
        parts_of_speech = ['NP','VP']
        tags = [['musical_instrument'],['make_music']]
    elif word_length == 3:
        parts_of_speech = ['NP','VP','D']
        tags = [['musical_instrument'],['make_music'],['positive','follow_verb']]
    elif word_length == 4:
        parts_of_speech = ['A','NP','VP','D']
        tags = [['positive','to_person'],['musical_instrument'],['make_music'],['positive','follow_verb']]
    elif word_length == 5:
        parts_of_speech = ['NP','VP','C','NP','VP']
        tags = [['musical_instrument'],['make_music'],[],['musical_instrument'],['make_music']]
    elif word_length == 6:
        parts_of_speech = ['NP','VP','C','NP','VP','D']
        tags = [['musical_instrument'],['make_music'],[],['musical_instrument'],['make_music'],['positive','follow_verb']]
    elif word_length == 7:
        parts_of_speech = ['NP','VP','D','C','NP','VP','D']
        tags = [['musical_instrument'],['make_music'],['positive','follow_verb'],[],['musical_instrument'],['make_music'],['positive','follow_verb']]
    elif word_length == 8:
        parts_of_speech = ['A','NP','VP','D','C','NP','VP','D']
        tags = [['to_person','positive'],['musical_instrument'],['make_music'],['positive','follow_verb'],[],['musical_instrument'],['make_music'],['positive','follow_verb']]
    elif word_length == 9:
        parts_of_speech = ['A','NP','VP','D','C','A','NP','VP','D']
        tags = [['positive','to_person'],['musical_instrument'],['make_music'],['positive','follow_verb'],[],['to_person','positive'],['musical_instrument'],['make_music'],['positive','follow_verb']]
    elif word_length == 10:
        parts_of_speech = ['A','A','NP','VP','D','C','A','NP','VP','D']
        tags = [['to_person','positive'],['to_person','positive'],['musical_instrument'],['make_music'],['positive','follow_verb'],[],['to_person','positive'],['musical_instrument'],['make_music'],['positive','follow_verb']]
    elif word_length == 11:
        parts_of_speech = ['NP','VP','D','C','NP','VP','D','C','NP','VP','D']
        tags = [['musical_instrument'],['make_music'],['positive','follow_verb'],[],['musical_instrument'],['make_music'],['positive','follow_verb'],[],['musical_instrument'],['make_music'],['positive','follow_verb']]
    else:
        if word_length % 4 == 0:
            tags.append(['positive','to_person'])
            parts_of_speech.append('A')
            
        elif word_length % 4 == 1:
            tags.append(['positive','to_person'])
            parts_of_speech.append('A')
            
            tags.append(['positive','to_person'])
            parts_of_speech.append('A')

        elif word_length % 4 == 2:

            tags.append(['positive','to_person'])
            parts_of_speech.append('A')
            
            tags.append(['positive','to_person'])
            parts_of_speech.append('A')
            
            tags.append(['positive','to_person'])
            parts_of_speech.append('A')

        counter = 0
        while counter < word_length:
            parts_of_speech.append('NP')
            parts_of_speech.append('VP')
            parts_of_speech.append('D')
                
            tags.append(['musical_instrument'])
            tags.append(['make_music'])
            tags.append(['positive','follow_verb'])
            
            if counter + 3 < word_length:
                parts_of_speech.append('C')
                tags.append([])
            
            counter += 4

    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, parts_of_speech[word_num])
    add_tag_list_filter(filters, tags[word_num])
    
    return [filters, parts_of_speech[word_num], condense_tags_list(tags[word_num])]
    