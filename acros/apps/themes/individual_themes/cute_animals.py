"""
file        :   cute_animals.py
date        :   2015-03-10
module      :   themes
classes     :
description :   constructions associated with cute_animals theme
"""

from apps.themes.utils.generic_constructions import all_same, pos1_pos2
from apps.themes.utils.generic_constructions import E_A_NP_VP_D_C_pattern

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