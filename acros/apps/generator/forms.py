"""
file        :   forms.py
date        :   2014-1030
module      :   generator
classes     :   GeneratorFromView
desription  :   forms for word generator
"""

from django import forms

from .models import Word



class GenerateAcrosticForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ['name']
    
    name = forms.CharField(
        max_length=50,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control input-tall control-label',
                'id': 'vertical-word',
                'type': 'text',
                'name': 'name',
                'placeholder': 'Enter vertical word',
            }
        )
    )