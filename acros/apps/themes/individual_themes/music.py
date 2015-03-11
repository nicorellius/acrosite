"""
file        :   music.py
date        :   2015-03-10
module      :   themes
classes     :
description :   constructions associated with music theme
"""

from apps.themes.utils.generic_constructions import all_same
from apps.themes.utils.generic_constructions import E_A_NP_VP_D_C_pattern, E_A_NP1_VP_NP2_D_C_pattern

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