"""
file        :   music.py
date        :   2015-03-10
module      :   themes
classes     :
description :   constructions associated with music theme
"""

from apps.themes.utils.generic_constructions import all_same
from apps.themes.utils.generic_constructions import connected_intransitive_verbs, connected_transitive_verbs

from apps.constants import pos

def animals_jamming(vert_word, word_list):
    
    pos_tags_master = {
        pos.EXCLAMATION : [],
        pos.ADJECTIVE : ['positive','cute_animal_theme'],
        pos.NOUN_PLURAL_FIRST : ['cute_animal'],
        pos.VERB_PLURAL : ['operate_musical_instrument'],
        pos.NOUN_PLURAL_SECOND : ['musical_instrument'],
        pos.ADVERB : ['follow_verb','positive'],
        pos.CONNECTING_EXPRESSION : [],
    }
    
    return connected_transitive_verbs(pos_tags_master, vert_word, word_list)

def just_instruments(vert_word, word_list):
    return all_same(pos.NOUN_PLURAL, ['musical_instrument'], vert_word, word_list)

def instruments_making_music(vert_word, word_list):
    
    pos_tags_master = {
        pos.EXCLAMATION : [],
        pos.ADJECTIVE : ['positive', 'to_person'],
        pos.NOUN_PLURAL : ['musical_instrument'],
        pos.VERB_PLURAL : ['produce_music'],
        pos.ADVERB : ['follow_verb','positive'],
        pos.CONNECTING_EXPRESSION : [],
    }
    
    return connected_intransitive_verbs(pos_tags_master,vert_word, word_list)