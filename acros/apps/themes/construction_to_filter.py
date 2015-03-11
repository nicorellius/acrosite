"""
file        :   construction_to_filter.py
date        :   2015-01-18
module      :   themes
classes     :
description :   intermediary between generator and individual constructions
"""

from apps.themes.individual_themes.my_name import my_name_adj
from apps.themes.individual_themes.my_name import my_name_adv_adj

from apps.themes.individual_themes.cute_animals import cute_animals_verbs
from apps.themes.individual_themes.cute_animals import cute_animals_adj_noun
from apps.themes.individual_themes.cute_animals import just_cute_animals

from apps.themes.individual_themes.music import instruments_making_music
from apps.themes.individual_themes.music import animals_jamming
from apps.themes.individual_themes.music import just_instruments


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