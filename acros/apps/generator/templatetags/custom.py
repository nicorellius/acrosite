'''
Created on Nov 19, 2014

@author: phillipseitzer
'''

from django import template

register = template.Library()

@register.filter(name='usplit')
def usplit(value, arg):
    return value.split(arg)

@register.filter(name='acrosticize')
def acrosticize(value):
    string_array = value.split(";")
    formatted_text = "<br>"
    for word in string_array:
        if word:
            word_chars = list(word)
            first_character = True
            for char in word_chars:
                if first_character:
                    formatted_text = (formatted_text 
                    + "<strong>" 
                    + "<font color=\"red\" face=\"courier\" size=\"4\">"
                    + char.upper() 
                    + "</font>"
                    + " "
                    + "</strong>"
                    )
                else:
                    formatted_text = formatted_text + char.lower()
                first_character = False   
            formatted_text = formatted_text + "<br>"
    return formatted_text
