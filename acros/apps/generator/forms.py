"""
file        :   forms.py
date        :   2014-1030
module      :   generator
classes     :   GeneratorFromView
desription  :   forms for word generator
"""

from django import forms

from .models import Word



class GenerateAcrosticForm():

    class Meta:
        model = Word
        fields = ['word',]
    
    word = forms.CharField(
        max_length=50,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control control-label',
                'type': 'text',
                'name': 'name',
                'placeholder': 'enter name',
            }
        )
    )