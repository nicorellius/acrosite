"""
file        :   cute_animals.py
date        :   2015-03-10
module      :   themes
classes     :
description :   constructions associated with cute_animals theme
"""

from apps.themes.utils.generic_constructions import all_same, pos1_pos2
from apps.themes.utils.generic_constructions import E_A_NP_VP_D_C_pattern

from apps.constants import pos

def cute_animals_verbs(vert_word, word_list):
    
    pos_tags_master = {
        pos.EXCLAMATION : [],
        pos.ADJECTIVE : ['cute_animal_theme','positive'],
        pos.NOUN_PLURAL : ['cute_animal'],
        pos.VERB_PLURAL : ['cute_animal_theme','positive'],
        pos.ADVERB : ['follow_verb','positive'],
        pos.CONNECTING_EXPRESSION : [],
    }
    
    return E_A_NP_VP_D_C_pattern(pos_tags_master,vert_word, word_list)

def cute_animals_adj_noun(vert_word, word_list):
    
    pos_tags_master = {
    pos.ADJECTIVE : ['cute_animal_theme','positive'],
    pos.NOUN_PLURAL : ['cute_animal'],
    }
    
    return pos1_pos2(pos.ADJECTIVE, pos.NOUN_PLURAL, pos_tags_master, vert_word, word_list)

def just_cute_animals(vert_word, word_list):
    return all_same(pos.NOUN_PLURAL, ['cute_animal'], vert_word, word_list)