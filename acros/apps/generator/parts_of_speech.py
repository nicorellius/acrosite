"""
file        :   parts_of_speechs.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   A repository for different sorts of parts_of_speechs.

KEY:
N = noun - use `noun`
V = verb - use `verb`
A = adjective - use `adj`
D = adverb - use `adv`

P = plural (modifies above 4) - use `plu`
S = singular (modifies above 4) - use `sin`
"""

def adj_to_noun(vertical_word, is_plural):
    
    characters = list(vertical_word)
    
    counter = 1
    parts_of_speech = []

    while counter < len(characters):
        parts_of_speech.append('A')
        counter += 1

    if is_plural:
        parts_of_speech.append('NP')
    else:
        parts_of_speech.append('NS')
    
    return parts_of_speech


def adj_to_noun_verb_adv(vertical_word, is_plural):
    
    characters = list(vertical_word)
    
    counter = 1
    parts_of_speech = []

    if len(characters) == 1:
        parts_of_speech = ['A']

    elif len(characters) == 2:

        if is_plural:
            parts_of_speech = ['A','NP']
        else:
            parts_of_speech = ['A','NS']

    elif len(characters) == 3:
        
        if is_plural:
            parts_of_speech = ['A','A','NP']
        else:
            parts_of_speech = ['A','A','NS']

    else:
        counter = 3

        while counter < len(characters):
            parts_of_speech.append('A')
            counter += 1

        if is_plural:
            parts_of_speech.append('NP')
            parts_of_speech.append('VP')
            parts_of_speech.append('D')
        else:
            parts_of_speech.append('NS')
            parts_of_speech.append('VS')
            parts_of_speech.append('D')

    return parts_of_speech
    
       
def adj_adj_noun_pattern(vertical_word, is_plural):

    """
    when the vertical_word has more than 3 letters,
    repeat adjective-adjective-noun, otherwise, handle specially.
    """

    characters = list(vertical_word)
    
    counter = 0
    parts_of_speech = []

    if len(characters) == 1:
        if is_plural:
            parts_of_speech = ['NP']
        else:
            parts_of_speech = ['NS']
    elif len(characters) == 2:
        if is_plural:
            parts_of_speech = ['A','NP']
        else:
            parts_of_speech = ['A','NS']
    else:
        while counter < len(characters):
            if counter % 3 == 2:
                if is_plural:
                    parts_of_speech.append('NP')
                else:
                    parts_of_speech.append('NS')
            else:
                parts_of_speech.append('A')
            counter += 1

        if counter % 3 == 1:
            del parts_of_speech[-3]
            if is_plural:
                parts_of_speech.append('NP')
                parts_of_speech.append('A')
                parts_of_speech.append('NP')
            else:
                parts_of_speech.append('NS')
                parts_of_speech.append('A')
                parts_of_speech.append('NS')
                
        elif counter % 3 == 2:
            del parts_of_speech[-1]
            if is_plural:
                parts_of_speech.append('NP')
            else:
                parts_of_speech.append('NS')
            
    return parts_of_speech



def all_adj(vertical_word):
    
    characters = list(vertical_word)
    return ['A'] * len(characters)



def all_nouns(vertical_word, is_plural):
    
    characters = list(vertical_word)
    if is_plural:
        return ['NP'] * len(characters)
    else:
        return ['NS'] * len(characters)