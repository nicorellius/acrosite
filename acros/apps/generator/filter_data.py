'''
Created on Jan 18, 2015

@author: phillipseitzer
'''
import random
from django.db.models import Q
from .parts_of_speech import adj_to_noun_verb_adv, adj_to_noun, adj_adj_noun_pattern, all_adj, all_nouns
from .tags import same_except_last

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
        parts_of_speech = adj_to_noun_verb_adv(vert_word, True)
    elif construction_type == 2:
        parts_of_speech = adj_to_noun(vert_word, True);
    elif construction_type == 3:
        parts_of_speech = adj_adj_noun_pattern(vert_word, True);
    elif construction_type == 4:
        parts_of_speech = adj_adj_noun_pattern(vert_word, False);
    elif construction_type == 5:
        parts_of_speech = all_adj(vert_word)
    elif construction_type == 6:
        parts_of_speech = all_nouns(vert_word, True)
    elif construction_type == 7:
        parts_of_speech = all_nouns(vert_word, False)
    
    # initialize empty
    filter_set = [];
    counter = 0;
    
    characters = list(vert_word)
        
    while counter < len(characters):
        filters = []
        add_first_letter_filter(filters, characters[counter])
        add_part_of_speech(filters, parts_of_speech[counter])
        add_theme(filters,'cute_animals')
        if (parts_of_speech[counter] == 'A'):
            add_tag(filters, 'positive')
        
        filter_set.append(filters)
        counter += 1
    
    return [filter_set,parts_of_speech,[]]



def politics(vert_word, construction_type):
    
    print('Building politics acrostic with construction type {0}'.format(construction_type))
 
    if construction_type == 1:
        parts_of_speech = adj_to_noun(vert_word, False)
        tags = same_except_last(vert_word, 'positive','idea')
    elif construction_type == 2:
        parts_of_speech = adj_to_noun(vert_word, True)
        tags = same_except_last(vert_word, 'positive','person')
    elif construction_type == 3:
        parts_of_speech = adj_to_noun(vert_word, False)
        tags = same_except_last(vert_word, 'negative','idea')
    elif construction_type == 4:
        parts_of_speech = adj_to_noun(vert_word, True)
        tags = same_except_last(vert_word, 'negative','person')
    
    filter_set = [];
    counter = 0;
    
    characters = list(vert_word)
    
    while counter < len(characters):
        filters = []
        add_first_letter_filter(filters, characters[counter])
        add_part_of_speech(filters, parts_of_speech[counter])
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
    
    parts_of_speech = []
    tags = []
    filter_set = []
    
    for character in characters:
        parts_of_speech.append('NP')
        tags.append('instrument')
        filters = []
        add_first_letter_filter(filters, character)
        add_part_of_speech(filters, 'NP')
        add_tag(filters, 'instrument')
        add_theme(filters, 'music')
        filter_set.append(filters)
    
    return [filter_set, parts_of_speech, tags] 



def create_acrostic_filter_data(vert_word, theme_name, construction_type):
    
    acrostic_data = []
    
    if theme_name=='cute_animals':
              
        acrostic_data = cute_animals(vert_word, construction_type)
        
    elif theme_name=='music':
               
        if construction_type == 1:
            acrostic_data = animals_jamming(vert_word)
        elif construction_type == 2:
            acrostic_data = just_instruments(vert_word)
                
    elif theme_name=='politics':
    
        acrostic_data = politics(vert_word, construction_type)
        
    return acrostic_data
    