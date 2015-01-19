'''
Created on Jan 18, 2015

@author: phillipseitzer
'''

from django.db.models import Q
from .constructions import adj_to_noun_verb_adv

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

def cute_animals_cute(vert_word):
    
    # retrieve original constructions
    constr = adj_to_noun_verb_adv(vert_word, True)
    parts_of_speech = constr.get_list()
    characters = list(vert_word)
    
    # initialize empty
    filter_set = [];
    counter = 0;
    
    for part_of_speech in parts_of_speech:
        filters = []
        letter = characters[counter]
        add_first_letter_filter(filters, letter)
        add_part_of_speech(filters, part_of_speech)
        add_theme(filters,'cute_animals')
        
        filter_set.append(filters)
        counter += 1
    
    return filter_set

# TODO: This function is called from generate, and produces
# the appropriate set of filters for these objects.
def create_filter_set(vert_word, theme_name, build_id):
    return
    