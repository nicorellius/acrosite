'''
Created on Jan 25, 2015

@author: phillipseitzer
'''
from django.db.models import Q

def add_first_letter_filter(filters, letter):
    filters.append(Q(name__startswith=letter),)
    return filters

def add_tag_filter(filters, tag):
    filters.append(Q(tags__contains=tag),)
    return filters

def add_tag_list_filter(filters, tag_list):
    for tag in tag_list:
        add_tag_filter(filters, tag)
    return filters

def add_part_of_speech_filter(filters, pos):
    filters.append(Q(part_of_speech=pos),)
    return filters

def add_pos_OR_filter(filters, pos1, pos2):
    filters.append((Q(part_of_speech=pos1) | Q(part_of_speech=pos2)))
    return filters

def add_tag_OR_filter(filters, tag1, tag2):
    filters.append((Q(tags__contains=tag1) | Q(tags__contains=tag2)))
    return filters

def condense_tags_list(tag_list_list):
    formatted_tag_list = []
    for tag_list in tag_list_list:
        formatted_tag_list.append(";".join(tag_list))
    
    return formatted_tag_list