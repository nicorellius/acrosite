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
    constr = ''

    while counter < len(characters):
        constr = constr + 'A;'
        counter += 1

    constr = constr + 'NS;'
    
    construction = Construction()
    construction.sequence = constr
    construction.constr_id = 'all-adjectives-except-last-noun'
    
    return construction


def adj_to_noun_sin_verb_sin_adj(vertical_word):  # A_to_NS_VS_D
    
    characters = list(vertical_word)
    
    counter = 1
    constr = ''

    if len(characters) == 1:
        constr = 'A;'

    elif len(characters) == 2:
        constr = 'A;NP;'

    elif len(characters) == 3:
        constr = 'A;A;NP;'

    else:
        counter = 3

        while counter < len(characters):
            constr = constr + 'A;'
            counter += 1

        constr = constr + 'NP;VP;D;'
    
    print(constr)
    
    construction = Construction()
    construction.sequence = constr
    construction.constr_id = 'adjectives-to-NP-VP-D'
    
    return construction
    

# when the vertical_word has more than 3 letters, repeat adjective-adjective-noun,
# otherwise, handle specially.
def adj_adj_noun_pattern(vertical_word):  # AA_N_pattern
    
    characters = list(vertical_word)
    
    counter = 0
    constr = ""

    while counter < len(characters):

        if counter % 3 == 2:
            constr = constr + 'N;'

        else:
            constr = constr + 'A;'

        counter += 1
    
    # modify for various special cases
    if counter < 3:
        constr = constr[:-2] + 'N;'

    elif counter % 3 != 0:
        constr = constr[:-2] + 'N;'
        
    construction = Construction()
    construction.sequence = constr
    construction.constr_id = 'AA-N-pattern'
    
    return construction
