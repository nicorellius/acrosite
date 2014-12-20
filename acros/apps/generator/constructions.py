"""
file        :   constructions.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   A repository for different sorts of constructions.
"""
from .models import Construction

"""
KEY:
N = noun - use `noun`
V = verb - use `verb`
A = adjective - use `adj`
D = adverb - use `adv`

P = plural (modifies above 4) - use `plu`
S = singular (modifies above 4) - use `sin`
"""


def adj_to_noun(vertical_word):  # A_to_N
    
    characters = list(vertical_word)
    
    counter = 1
    sequence = ''

    while counter < len(characters):
        sequence += 'A;'
        counter += 1

    sequence += 'NS;'
    
    construction = Construction()
    construction.sequence = sequence
    construction.description = 'all-adjectives-except-last-noun'
    construction.save()
    
    return construction


def adj_to_noun_sin_verb_sin_adj(vertical_word):  # A_to_NS_VS_D
    
    characters = list(vertical_word)
    
    counter = 1
    sequence = ''

    if len(characters) == 1:
        sequence = 'A;'

    elif len(characters) == 2:
        sequence = 'A;NP;'

    elif len(characters) == 3:
        sequence = 'A;A;NP;'

    else:
        counter = 3

        while counter < len(characters):
            sequence += 'A;'
            counter += 1

        sequence += 'NP;VP;D;'
    
    print(sequence)
    
    construction = Construction()
    construction.sequence = sequence
    construction.description = 'adjectives-to-NP-VP-D'
    construction.save()
    
    return construction
    

def adj_adj_noun_pattern(vertical_word):  # AA_N_pattern

    """
    when the vertical_word has more than 3 letters,
    repeat adjective-adjective-noun, otherwise, handle specially.
    """

    characters = list(vertical_word)
    
    counter = 0
    sequence = ""

    while counter < len(characters):

        if counter % 3 == 2:
            sequence += 'N;'

        else:
            sequence += 'A;'

        counter += 1
    
    # modify for various special cases
    if counter < 3:
        sequence = sequence[:-2] + 'N;'

    elif counter % 3 != 0:
        sequence = sequence[:-2] + 'N;'
        
    construction = Construction()
    construction.sequence = sequence
    construction.description = 'AA-N-pattern'
    construction.save()
    
    return construction
