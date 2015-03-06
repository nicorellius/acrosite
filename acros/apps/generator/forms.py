"""
file        :   forms.py
date        :   2014-10-30
module      :   generator
classes     :   GeneratorFromView
description :   forms for word generator
"""

from django import forms

from .models import Word, Acrostic


class GenerateAcrosticForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ['name', 'theme']

    THEME_CHOICES = (
        ('default', 'Choose a theme'),
        ('my_name', 'My name'),
        ('cute_animals', 'Cute animals'),
        ('music', 'Music'),
    )
    
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-tall control-label',
                'id': 'vertical-word',
                'type': 'text',
                'name': 'name',
                'placeholder': 'Enter your name or another word',
            }
        )
    )

    theme = forms.ChoiceField(
        choices=THEME_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'bootstrap-select show-tick',
                'id': 'theme-selector',
                'type': 'button',
                'name': 'theme',
                'data-live-search': 'true',
                'data-style': 'btn-success',
            }
        )
    )


class RateAcrosticForm(forms.ModelForm):

    class Meta:
        model = Acrostic
        fields = ['value']

    VALUE_CHOICES = (
        ('default', 0.0),
        ('point-five', 0.5),
        ('one', 1.0),
        ('one-point-five', 1.5),
        ('two', 2.0),
        ('two-point-five', 2.5),
        ('three', 3.0),
        ('three-point-five', 3.5),
        ('four', 4.0),
        ('four-point-five', 4.5),
        ('five', 5.0),
    )

    value = forms.ChoiceField(
        choices=VALUE_CHOICES,
        widget=forms.RadioSelect(
            attrs={}
        )
    )