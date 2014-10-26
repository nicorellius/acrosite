from django.db import models


class Word(models.Model):
    
    word = models.CharField(max_length=200)

    def __str__(self):
        return self.word
