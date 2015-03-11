"""
file        :   build_constructions.py
date        :   2015-01-18
module      :   generator
classes     :
description :   Build constructions for generating acrostics
"""

from apps.themes.utils.generic_constructions import all_same, pos1_pos2
from apps.themes.utils.generic_constructions import E_A_NP_VP_D_C_pattern, E_A_NP1_VP_NP2_D_C_pattern

def create_word_filter(vert_word, word_list, theme_name, construction_type):
    word_filter = []
    
    if theme_name == 'my_name':

        if construction_type == 1: 
            word_filter = my_name_adj(vert_word, word_list, True) # positive
        elif construction_type == 2:
            word_filter = my_name_adv_adj(vert_word, word_list, True)  # positive
        elif construction_type == 3:
            word_filter = my_name_adj(vert_word, word_list, False)  # negative
        elif construction_type == 4:
            word_filter = my_name_adv_adj(vert_word, word_list, False) # negative

    elif theme_name == 'cute_animals':
        if construction_type == 1:
            word_filter = cute_animals_verbs(vert_word, word_list)
        elif construction_type == 2:
            word_filter = cute_animals_adj_noun(vert_word, word_list)
        elif construction_type == 3:
            word_filter = just_cute_animals(vert_word, word_list)

    elif theme_name == 'music':
        if construction_type == 1:
            word_filter = instruments_making_music(vert_word, word_list)
        elif construction_type == 2:
            word_filter = animals_jamming(vert_word, word_list)
        elif construction_type == 3:
            word_filter = just_instruments(vert_word, word_list)
            
    return word_filter


def my_name_adj(vert_word, word_list, is_positive):
    
    if is_positive:
        positivity_tag = 'positive'
    else:
        positivity_tag = 'negative'
        
    return all_same('A',[positivity_tag,'to_person'],vert_word, word_list)

def my_name_adv_adj(vert_word, word_list, is_positive):
    
    if is_positive:
        positivity_tag = 'positive'
    else:
        positivity_tag = 'negative'
    
    pos_tags_master = {       
        'D':['precede_adjective',positivity_tag],
        'A':['to_person',positivity_tag],
    }
    
    return pos1_pos2('D','A', pos_tags_master, vert_word, word_list)


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

def cute_animals_adj_noun(vert_word, word_list):
    
    pos_tags_master = {
    'A':['cute_animal_theme','positive'],
    'NP':['cute_animal'],
    }
    
    return pos1_pos2('A', 'NP', pos_tags_master, vert_word, word_list)

def just_cute_animals(vert_word, word_list):
    return all_same('NP',['cute_animal'],vert_word, word_list)

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
    return all_same('NP',['musical_instrument'],vert_word, word_list)

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
