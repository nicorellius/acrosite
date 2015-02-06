"""
file        :   forms.py
date        :   2014-10-30
module      :   generator
classes     :   GeneratorFromView
description :   forms for word generator
"""

from django import forms

from .models import Word


class GenerateAcrosticForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ['name', 'theme']

    THEME_CHOICES = (
        ('name', 'My Name'),
        ('cute-animals', 'Cute Animals'),
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
                'placeholder': 'Enter your name or anther word',
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