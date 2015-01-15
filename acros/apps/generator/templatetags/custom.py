"""
file        :   custom.py
date        :   2014-11-19
module      :   generator.templatetags
classes     :   
description :   custom templatetags for generator app
"""

import re

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
                    # see styles.css, class acrostic-letter for this bit of styling
                    formatted_text = '{0}{1}{2}{3}'.format(
                        formatted_text,
                        '<span class="acrostic-letter">',
                        char.upper(),
                        '</span>'
                    )
                else:
                    formatted_text = formatted_text + char.lower()
                first_character = False

            formatted_text += "<br>"

    return formatted_text


@register.filter(name='prettify')
def prettify(value, delimiter):

    value = re.sub('_', delimiter, value)
    value = value.title()

    return value