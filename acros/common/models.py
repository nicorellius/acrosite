"""
file        :   models.py
date        :   2014-1101
module      :   common
classes     :   BaseModel
desription  :   base model for all other models
"""

from django.db import models

class BaseModel (models.Model):
    
    """
    Abstract base class model that provides self-updating `created` and `modified` fields.
    It also provides slug and description fields that are common to all models.
    """
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="create date")
    modified = models.DateTimeField(auto_now=True, verbose_name="modified date")
    slug = models.SlugField(help_text='slug for URLs')
    description = models.TextField(blank=True)
    
    class Meta:
        abstract = True