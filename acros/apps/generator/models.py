"""
file        :   models.py
date        :   2014-1101
module      :   generator
classes     :   Word
desription  :   models for word generator
"""

from django.db import models
#from magic import get_format 
# @UnresolvedImport
from . import magic #@UnresolvedImport
from . import populate

# check out common/models.py for BaseModel definition
from common.models import BaseModel  # @UnresolvedImport
#from apps.generator.populate import basic_word_list

class Word(BaseModel):
    
    name = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=200)
    themes = models.CharField(max_length=200)
    valuation = models.FloatField()
    
    def __str__(self):
        return self.name
    
class Acrostic(BaseModel):
    
    vertical_word = models.CharField(max_length=200, default = 'N/A')
    horizontal_words = models.CharField(max_length=200, default = 'N;/;A')
    construction = models.CharField(max_length=200)
    construction_name = models.CharField(max_length=200, default= 'Anything')
    theme = models.CharField(max_length=200, default= 'ALL_CATEGORIES')
    
    def __str__(self):
        component_words = self.horizontal_words.split(';')
        str = ""
        for word in component_words:
            str = str + word + "\n"
        return str
    
    def generate_random_acrostic(self, vert_word):
        self.vertical_word = vert_word
        
        print("Part of speech: ", magic.get_format(vert_word)) 
        
        basic_words = self.basic_word_list()
        
        if vert_word.upper() == 'TEST':
            self.horizontal_words = "Take;Every;Single;Tangerine"
        else: 
            characters = list(vert_word) #returns array of characters
            str = ""
            for letter in characters:
                for word in basic_words:
                    print(word.name, letter, word.name.startswith(letter))
                    if word.name.startswith(letter):
                        letter = word.name
                str = str + letter + ";"
            self.horizontal_words = str
        print("Acrostic: ", self.horizontal_words);
        return self.horizontal_words
    
    def basic_word_list(self):
        word1 = Word()
        word1.name = "apple"
        word1.part_of_speech = "NN"
        word1.themes = "fruits;"
    
        word2 = Word()
        word2.name = "banana"
        word2.part_of_speech = "NN"
        word2.themes = "fruits;"
    
        word3 = Word()
        word3.name = "cockroach"
        word3.part_of_speech = "NN"
        word3.themes ="insects;gross"
    
        word4 = Word()
        word4.name = "dancing"
        word4.part_of_speech = "V"
        word4.themes = "party;romantic"
    
        word5 = Word()
        word5.name = "elephant"
        word5.part_of_speech = "NN"
        word5.themes = "animal;circus"
        
        word6 = Word()
        word6.name = "is"
        word6.part_of_speech = "V"
        word6.themes = ""
        
        word7 = Word()
        word7.name = "overindulgently"
        word7.part_of_speech ="ADV"
        word7.themes = "long;negative"
        
        word8 = Word()
        word8.name = "ugly"
        word8.part_of_speech ="ADJ"
        word8.themes ="negative"
        
        word9 = Word()
        word9.name = "terrible"
        word9.part_of_speech = "ADJ"
        word9.themes = "negative"
        
        word10 = Word()
        word10.name = "randy"
        word10.part_of_speech = "ADJ"
        word10.themes = "BritishProfanity;names"
        
        word_list = [word1, word2, word3, word4, word5,
                     word6, word7, word8, word9, word10]
        return word_list