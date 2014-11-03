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

    def __str__(self):
        return self.word