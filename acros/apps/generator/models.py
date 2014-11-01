"""
file        :   models.py
date        :   2014-1101
module      :   generator
classes     :   Word
desription  :   models for word generator
"""

from django.db import models

from common.models import BaseModel



class Word(BaseModel):
    
    word = models.CharField(max_length=200)

    def __str__(self):
        return self.word