'''
Created on Jan 18, 2015

@author: phillipseitzer
'''

def all_tag(vertical_word, tag):
    
    characters = list(vertical_word);
    sequence = '';
    for character in characters:
        sequence += tag
        
    return sequence