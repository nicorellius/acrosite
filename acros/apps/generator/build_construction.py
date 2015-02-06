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

def create_acrostic_data(vert_word, theme_name, construction_type):
    
    acrostic_data = []
    
    if theme_name=='cute_animals':
        if construction_type <= 4:
            acrostic_data = cute_animals_theme(vert_word, construction_type)
        
    elif theme_name=='music':
               
        if construction_type == 1:
            acrostic_data = animals_jamming(vert_word)
        elif construction_type == 2:
            acrostic_data = just_instruments(vert_word)
        elif construction_type == 3:
            acrostic_data = exclamation_animals_jamming(vert_word)
        elif construction_type == 4:
            acrostic_data = instruments_making_music(vert_word);
    '''  
    elif theme_name=='politics':
    
        if construction_type == 1 or construction_type == 2:
            acrostic_data = politics_theme(vert_word, construction_type)
        elif construction_type == 3:
            acrostic_data = political_figure_question(vert_word)
    '''        
    return acrostic_data

def create_filters(vert_word, word_list, theme_name, construction_type):
    acrostic_data = []
    
    if theme_name == 'my_name':
        '''
        [1,2] have equal priority. 3 and 4 are hidden types, which are
        realized when 1 or 2 is selected, and then there is 1/3 chance that
        1 or 2 will be converted to 3 or 4.  1 and 3 are the same (except positive)
        2 and 4are the same (except negative).
        '''
        if construction_type == 1:
            acrostic_data = adjectives(vert_word, word_list, True)
        elif construction_type == 2:
            acrostic_data = adv_adj(vert_word, word_list, True)
        elif construction_type == 3:
            acrostic_data = adjectives(vert_word, word_list, False)
        elif construction_type == 4:
            acrostic_data = adv_adj(vert_word, word_list, False)
    elif theme_name == 'cute_animals':
        acrostic_data = cute_animals_theme_rewrite(vert_word, word_list, construction_type)
    elif theme_name == 'music':
        if construction_type == 1:
            acrostic_data = instruments_making_music(vert_word, word_list)
        elif construction_type == 2:
            acrostic_data = animals_jamming(vert_word, word_list)
        elif construction_type == 3:
            acrostic_data = just_instruments(vert_word, word_list)
            
    return acrostic_data

def adjectives(vert_word, word_list, is_positive):
    
    part_of_speech = 'A'
    if is_positive:
        tags = ['positive']
    else:
        tags = ['negative']    
        
    characters = list(vert_word)
    word_num = len(word_list)

    filters = []
    add_first_letter_filter(filters, characters[word_num])
    add_part_of_speech_filter(filters, part_of_speech)
    add_tag_list_filter(filters, tags)

    return [filters, part_of_speech, tags]



def adv_adj(vert_word, word_list, is_positive):

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
                
    filters = []
    
    add_first_letter_filter(filters, characters[len(word_list)])
    add_tag_list_filter(filters, tags)
    add_part_of_speech_filter(filters, part_of_speech)
    
    return [filters, part_of_speech, tags]

def cute_animals_theme(vert_word, construction_type):
    
    # retrieve original constructions
    if construction_type == 1:
        parts_of_speech = adj_to_noun_verb_adv(vert_word, True)
    elif construction_type == 2:
        parts_of_speech = adj_to_noun(vert_word, True);
    elif construction_type == 3:
        parts_of_speech = adj_adj_noun_pattern(vert_word, True);
    elif construction_type == 4:
        parts_of_speech = all_nouns(vert_word, True)
    
    # initialize empty
    filter_set = []
    tags = []
    counter = 0;
    
    characters = list(vert_word)
        
    while counter < len(characters):
        filters = []
        tags_list = []
        add_first_letter_filter(filters, characters[counter])
        add_part_of_speech_filter(filters, parts_of_speech[counter])
        add_tag_filter(filters,'cute_animals')
        tags_list.append('cute_animals')
        if (parts_of_speech[counter] == 'A'):
            add_tag_filter(filters, 'positive')
            tags_list.append('positive')
        
        tags.append(tags_list)
        filter_set.append(filters)
        counter += 1
    
    return [filter_set,parts_of_speech,tags]

def cute_animals_theme_rewrite(vert_word, word_list, construction_type):
    
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
    
        tags = ['cute_animals']
        if parts_of_speech[word_num] == 'A':
            tags.append('positive')
        elif parts_of_speech[word_num] == 'NP':
            tags.append('animal')
        
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
    
    if word_length - word_num >= 4:
        part_of_speech = 'A'
        tags = ['positive']
    elif word_length - word_num == 3:
        part_of_speech = 'NP'
        tags = ['animal']
    elif word_length+ - word_num == 2:
        part_of_speech = 'VP'
        tags = ['make_music']
    elif word_length - word_num == 1:
        part_of_speech = 'NP'
        tags = ['instrument']
        
    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, part_of_speech)
    add_tag_list_filter(filters, tags)
    
    return [filters, part_of_speech, tags]

#TODO: merge with animals_jamming
def exclamation_animals_jamming(vert_word):
    
    constr = []
    tags = []
    
    characters = list(vert_word)
    
    if len(characters) == 1:
        constr = ['NP']
        tags = [['instrument','music']]
    elif len(characters) == 2:
        constr = ['NP','VP']
        tags = [['animal'],['make_music']]
    elif len(characters) == 3:
        constr = ['NP','VP','NP']
        tags = [['animal'],['make_music'],['instrument','music']]
    elif len(characters) == 4:
        constr = ['NP','VP','NP','D']
        tags = [['animal'],['make_music'],['instrument','music'],['positive','cute_animals']]
    elif len(characters) == 5:
        constr = ['E','NP','VP','NP','D']
        tags = [['exclamation','positive'],['animal'],['make_music'],['instrument','music'],['positive','cute_animals']]
    else:
        counter = 5;
        constr = ['E']
        tags = [['exclamation','positive']]
        while counter < len(characters):
            constr.append('A')
            tags.append(['positive'])
            counter += 1
        
        constr.append('NP')
        constr.append('VP')
        constr.append('NP')
        constr.append('D')
        
        tags.append(['animal'])
        tags.append(['make_music'])
        tags.append(['instrument','music'])
        tags.append(['positive','cute_animals'])
    
    
    filter_set = []
    counter = 0
    while counter < len(characters):
        filters = []
        add_first_letter_filter(filters, characters[counter])
        add_part_of_speech_filter(filters, constr[counter])
        add_tag_list_filter(filters, tags[counter])
        filter_set.append(filters)
        counter += 1
    
    
    formatted_tags = condense_tags_list(tags)
    return [filter_set, constr, formatted_tags]
    
    
def just_instruments(vert_word, word_list):
    
    filters = []
    part_of_speech = 'NP'
    tags = ['instrument','music']
    
    characters = list(vert_word)
    
    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, part_of_speech)
    add_tag_list_filter(filters, tags)
    
    return [filters, part_of_speech, tags]


# TODO: handle punctuation appropriately, possibly reformat entirely
def instruments_making_music(vert_word, word_list):
    
    tags = []
    filters = []
    parts_of_speech = []
    
    characters = list(vert_word)
    word_length = len_valid_characters(characters)
    word_num = len_valid_words(word_list)
    
    if word_length == 1:
        parts_of_speech = ['NP']
        tags = [['instrument','music']]
    elif word_length == 2:
        parts_of_speech = ['NP','VP']
        tags = [['instrument','music'],['make_music']]
    elif word_length == 3:
        parts_of_speech = ['NP','VP','D']
        tags = [['instrument','music'],['make_music'],['positive']]
    elif word_length == 4:
        parts_of_speech = ['A','NP','VP','D']
        tags = [['positive'],['instrument','music'],['make_music'],['positive']]
    elif word_length == 5:
        parts_of_speech = ['NP','VP','C','NP','VP']
        tags = [['instrument','music'],['make_music'],['connexpr'],['instrument','music'],['make_music']]
    elif word_length == 6:
        parts_of_speech = ['NP','VP','C','NP','VP','D']
        tags = [['instrument','music'],['make_music'],['connexpr'],['instrument','music'],['make_music'],['positive']]
    elif word_length == 7:
        parts_of_speech = ['NP','VP','D','C','NP','VP','D']
        tags = [['instrument','music'],['make_music'],['positive'],['connexpr'],['instrument','music'],['make_music'],['positive']]
    elif word_length == 8:
        parts_of_speech = ['A','NP','VP','D','C','NP','VP','D']
        tags = [['positive'],['instrument','music'],['make_music'],['positive'],['connexpr'],['instrument','music'],['make_music'],['positive']]
    elif word_length == 9:
        parts_of_speech = ['A','NP','VP','D','C','A','NP','VP','D']
        tags = [['positive'],['instrument','music'],['make_music'],['positive'],['connexpr'],['positive'],['instrument','music'],['make_music'],['positive']]
    elif word_length == 10:
        parts_of_speech = ['A','A','NP','VP','D','C','A','NP','VP','D']
        tags = [['positive'],['positive'],['instrument','music'],['make_music'],['positive'],['connexpr'],['positive'],['instrument','music'],['make_music'],['positive']]
    elif word_length == 11:
        parts_of_speech = ['NP','VP','D','C','NP','VP','D','C','NP','VP','D']
        tags = [['instrument','music'],['make_music'],['positive'],['connexpr'],['instrument','music'],['make_music'],['positive'],['connexpr'],['instrument','music'],['make_music'],['positive']]
    else:
        if word_length % 4 == 0:
            tags.append(['positive'])
            parts_of_speech.append('A')
            
        elif word_length % 4 == 1:
            tags.append(['positive'])
            parts_of_speech.append('A')
            
            tags.append(['positive'])
            parts_of_speech.append('A')

        elif word_length % 4 == 2:

            tags.append(['positive'])
            parts_of_speech.append('A')
            
            tags.append(['positive'])
            parts_of_speech.append('A')
            
            tags.append(['positive'])
            parts_of_speech.append('A')

        counter = 0
        while counter < word_length:
            parts_of_speech.append('NP')
            parts_of_speech.append('VP')
            parts_of_speech.append('D')
                
            tags.append(['instrument','music'])
            tags.append(['make_music'])
            tags.append(['positive'])
            
            if counter + 3 < word_length:
                parts_of_speech.append('C')
                tags.append(['connexpr'])
            
            counter += 4

    add_first_letter_filter(filters, characters[len(word_list)])
    add_part_of_speech_filter(filters, parts_of_speech[word_num])
    add_tag_list_filter(filters, tags[word_num])
    
    return [filters, parts_of_speech[word_num], condense_tags_list(tags[word_num])]
    