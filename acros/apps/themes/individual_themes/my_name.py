"""
file        :   my_name.py
date        :   2015-03-10
module      :   themes
classes     :
description :   constructions associated with my_name theme
"""

from apps.themes.utils.generic_constructions import all_same, pos1_pos2

from apps.constants import pos

def my_name_adj(vert_word, word_list, is_positive):
    
    if is_positive:
        positivity_tag = 'positive'
    else:
        positivity_tag = 'negative'
        
    return all_same(pos.ADJECTIVE, [positivity_tag,'to_person'], vert_word, word_list)

def my_name_adv_adj(vert_word, word_list, is_positive):
    
    if is_positive:
        positivity_tag = 'positive'
    else:
        positivity_tag = 'negative'
    
    pos_tags_master = {       
        pos.ADVERB : ['precede_adjective',positivity_tag],
        pos.ADJECTIVE : ['to_person',positivity_tag],
    }
    
    return pos1_pos2(pos.ADVERB, pos.ADJECTIVE, pos_tags_master, vert_word, word_list)