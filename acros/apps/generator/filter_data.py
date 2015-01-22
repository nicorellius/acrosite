"""
file        :   filter_data.py
date        :   2015-01-18
application :   generator
classes     :
description :
"""

import random
from django.db.models import Q
from .constructions import adj_to_noun_verb_adv, adj_to_noun, adj_adj_noun_pattern, all_adj, all_nouns
from .tags import all_tag, same_except_last


def add_first_letter_filter(filters, letter):
    filters.append(Q(name__startswith=letter),)
    return filters


def add_theme(filters, theme_name):
    filters.append(Q(themes__contains=theme_name),)
    return filters


def add_tag(filters, tag):
    filters.append(Q(tags__contains=tag),)
    return filters


def add_part_of_speech(filters, pos):
    filters.append(Q(part_of_speech=pos),)
    return filters


def cute_animals(vert_word, construction_type):
    
    print('Building cute animals acrostic with construction type {0}'.format(construction_type))
    
    # retrieve original constructions
    if construction_type == 1:
        constr = adj_to_noun_verb_adv(vert_word, True)
    elif construction_type == 2:
        constr = adj_to_noun(vert_word, True);
    elif construction_type == 3:
        constr = adj_adj_noun_pattern(vert_word, True);
    elif construction_type == 4:
        constr = adj_adj_noun_pattern(vert_word, False);
    elif construction_type == 5:
        constr = all_adj(vert_word)
    elif construction_type == 6:
        constr = all_nouns(vert_word, True)
    elif construction_type == 7:
        constr = all_nouns(vert_word, False)
    parts_of_speech = constr.get_list()

    characters = list(vert_word)
    
    # initialize empty
    filter_set = [];
    counter = 0;
    
    for part_of_speech in parts_of_speech:
        filters = []
        add_first_letter_filter(filters, characters[counter])
        add_part_of_speech(filters, part_of_speech)
        add_theme(filters,'cute_animals')
        if (part_of_speech == 'A'):
            add_tag(filters, 'positive')
        
        filter_set.append(filters)
        counter += 1
    
    return [filter_set,parts_of_speech,[]]



def politics(vert_word, construction_type):
    
    print('Building politics acrostic with construction type {0}'.format(construction_type))
 
    if construction_type == 1:
        constr = adj_to_noun(vert_word, False)
        tags = same_except_last(vert_word, 'positive','idea')
    elif construction_type == 2:
        constr = adj_to_noun(vert_word, True)
        tags = same_except_last(vert_word, 'positive','person')
    elif construction_type == 3:
        constr = adj_to_noun(vert_word, False)
        tags = same_except_last(vert_word, 'negative','idea')
    elif construction_type == 4:
        constr = adj_to_noun(vert_word, True)
        tags = same_except_last(vert_word, 'negative','person')
        
    parts_of_speech = constr.get_list()
    
    characters = list(vert_word)
    
    filter_set = [];
    counter = 0;
    
    for part_of_speech in parts_of_speech:
        filters = []
        add_first_letter_filter(filters, characters[counter])
        add_part_of_speech(filters, part_of_speech)
        add_theme(filters,'politics')
        add_tag(filters, tags[counter])
        
        filter_set.append(filters)
        counter += 1
    
    return [filter_set,parts_of_speech,tags]


def animals_jamming(vert_word):
               
    characters = list(vert_word)
    
    if len(characters) == 1:
        constr = ['NP']
        tags = ['instrument']
    elif len(characters) == 2:
        constr = ['NP','VP']
        tags = ['animal','make_music']
    else:
        constr = ['NP','VP','NP']
        tags = ['animal','make_music','instrument']
    
    if len(characters) > 3:
        
        counter = 3
        while counter < len(characters):
            counter += 1
            constr.insert(0,'A')
            tags.insert(0,'positive')
    
    counter = 0
    
    filter_set = []
    while counter < len(constr):
        filters = []
        add_first_letter_filter(filters, characters[counter])
        add_part_of_speech(filters, constr[counter])
        add_tag(filters, tags[counter])
        filter_set.append(filters)
        counter += 1
            
    return [filter_set, constr, tags]



def just_instruments(vert_word):
    
    characters = list(vert_word)
    
    constr = []
    tags = []
    filter_set = []
    
    for character in characters:
        constr.append('NP')
        tags.append('instrument')
        filters = []
        add_first_letter_filter(filters, character)
        add_part_of_speech(filters, 'NP')
        add_tag(filters, 'instrument')
        add_theme(filters, 'music')
        filter_set.append(filters)
    
    return [filter_set, constr, tags] 



def create_acrostic_filter_data(vert_word, theme_name):
    
    acrostic_data = []
    
    cute_animal_types = [1,2,3,4,5,6,7]
    politics_types = [1,2,3,4]
    music_types = [1,2]
    
    if theme_name=='cute_animals':
        
        construction_and_tag_type = random.choice(cute_animal_types)
        acrostic_data = cute_animals(vert_word, construction_and_tag_type)
        
    elif theme_name=='music':
        
        construction_and_tag_type = random.choice(music_types)
        
        if construction_and_tag_type == 1:
            acrostic_data = animals_jamming(vert_word)
        elif construction_and_tag_type == 2:
            acrostic_data = just_instruments(vert_word)
                
    elif theme_name=='politics':
    
        construction_and_tag_type = random.choice(politics_types)
        acrostic_data = politics(vert_word, construction_and_tag_type)
        
    return acrostic_data