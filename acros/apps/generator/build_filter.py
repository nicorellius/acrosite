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

def condense_tags_to_list(tag_list_list):
    formatted_tag_list = []
    for tag_list in tag_list_list:
        formatted_tag_list.append(";".join(tag_list))
    
    return formatted_tag_list