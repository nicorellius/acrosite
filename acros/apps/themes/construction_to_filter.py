"""
file        :   construction_to_filter.py
date        :   2015-01-18
module      :   themes
classes     :
description :   intermediary between generator and individual constructions
"""

from apps.constants import constructions

from apps.themes.individual_themes.my_name import my_name_adj
from apps.themes.individual_themes.my_name import my_name_adv_adj

from apps.themes.individual_themes.cute_animals import cute_animals_verbs
from apps.themes.individual_themes.cute_animals import cute_animals_adj_noun
from apps.themes.individual_themes.cute_animals import just_cute_animals

from apps.themes.individual_themes.music import instruments_making_music
from apps.themes.individual_themes.music import animals_jamming
from apps.themes.individual_themes.music import just_instruments


def create_word_filter(vert_word, word_list, construction_type_ID):
    word_filter = []
    
    # theme = my name
    if construction_type_ID == constructions.MY_NAME_ADJ_POSITIVE:
        word_filter = my_name_adj(vert_word, word_list, True)
    elif construction_type_ID == constructions.MY_NAME_ADJ_ADV_POSITIVE:
        word_filter = my_name_adv_adj(vert_word, word_list, True)
    elif construction_type_ID == constructions.MY_NAME_ADJ_NEGATIVE:
        word_filter = my_name_adj(vert_word, word_list, False)
    elif construction_type_ID == constructions.MY_NAME_ADJ_ADV_NEGATIVE:
        word_filter = my_name_adv_adj(vert_word, word_list, False)
        
    # theme = cute animals
    elif construction_type_ID == constructions.CUTE_ANIMALS_INTRANSITIVE_VERB:
        word_filter = cute_animals_verbs(vert_word, word_list)
    elif construction_type_ID == constructions.CUTE_ANIMALS_ADJ:
        word_filter = cute_animals_adj_noun(vert_word, word_list)
    elif construction_type_ID == constructions.CUTE_ANIMALS_LIST:
        word_filter = just_cute_animals(vert_word, word_list)
        
    # theme = music
    elif construction_type_ID == constructions.INSTRUMENTS_MAKING_MUSIC:
        word_filter = instruments_making_music(vert_word, word_list)
    elif construction_type_ID == constructions.CUTE_ANIMALS_PLAYING_MUSIC:
        word_filter = animals_jamming(vert_word, word_list)
    elif construction_type_ID == constructions.MUSICAL_INSTRUMENTS_LIST:
        word_filter = just_instruments(vert_word, word_list)
        
    return word_filter