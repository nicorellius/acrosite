'''
Created on Jan 18, 2015

@author: phillipseitzer
'''

def all_tag(vertical_word, tag):
    
    characters = list(vertical_word);
    tags_list = []
    for character in characters:
        tags_list.append(tag)
        
    return tags_list

def same_except_last(vertical_word, every_other_tag, last_tag):
    
    characters = list(vertical_word)
    tags_list = []
    counter = 0
    while ((counter+1) < len(characters)):
        tags_list.append(every_other_tag)
        counter += 1
    
    tags_list.append(last_tag)
    return tags_list