"""
file        :   models.py
date        :   2014-1101
module      :   generator
classes     :   Word
desription  :   models for word generator
"""

from django.db import models

# check out common/models.py for BaseModel definition
from common.models import BaseModel

class Word(BaseModel):
    
    name = models.CharField(max_length=200)
    acrostic_text = models.CharField(max_length=200, default='ACROSTIC GOES HERE')
    
    def __str__(self):
        return self.name
    
    def generate_acrostic(self):
        if self.name.lower() == 'SHIT'.lower():
            self.acrostic_text = 'So Happy It\'s Thursday'
        elif self.name.lower() == 'EBOLA'.lower():
            self.acrostic_text = 'Everybody Believes in Ongoing Love, Africa!'
        else:
            self.acrostic_text = 'Sorry, we could not generate an acrostic for your submission.'
        return self.acrostic_text