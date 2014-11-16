'''
Created on Nov 15, 2014

@author: phillipseitzer
'''
'''
from .models import Word

def basic_word_list():

    word1 = Word()
    word1.name = "apple"
    word1.part_of_speech = "NN"
    word1.themes = "fruits;"
    word1.save()
    
    word2 = Word()
    word2.name = "banana"
    word2.part_of_speech = "NN"
    word2.themes = "fruits;"
    word2.save()
    
    word3 = Word()
    word3.name = "cockroach"
    word3.part_of_speech = "NN"
    word3.themes ="insects;gross"
    word3.save()
    
    word4 = Word()
    word4.name = "dancing"
    word4.part_of_speech = "V"
    word4.themes = "party;romantic"
    word4.save()
    
    word_list = [word1, word2, word3, word4]
    return word_list
'''