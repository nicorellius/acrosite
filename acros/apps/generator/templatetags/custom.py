"""
file        :   custom.py
date        :   2014-11-19
module      :   generator.templatetags
classes     :   
description :   custom templatetags for generator app
"""
import re
import unicodedata

from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(name='usplit')
def usplit(value, arg):

    return value.split(arg)


@register.filter(name='acrosticize')
def acrosticize(value):

    string_array = value.split(";")

    formatted_text = ''

    for word in string_array:

        if word:

            word_chars = list(word)
            first_character = True

            for char in word_chars:

                if first_character:
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

@register.filter(name='slagify')
def slagify(value):
    """
    Converts to lowercase and converts spaces to hyphens. Also strips leading and
    trailing whitespace. Similar to slugify but leaves special characters.
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value.strip().lower()

    return mark_safe(re.sub('[-\s]+', '-', value))

