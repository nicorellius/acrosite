"""
file        :   populate.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   Populate the database with Word models.
"""

from .models import Word

def populate_database():
    import_negative_adjectives()
    import_common_nouns()
    return

def import_negative_adjectives():
    f = open("resources/top100NegativeAdjectives.txt")
    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Negative;"
        word.part_of_speech = "A"
        word.save()
    f.close()
    print("Imported negative adjectives.")
    return

def import_common_nouns():
    f = open("resources/top100CommonNouns.txt")
    for line in f:
        word = Word()
        L = line.split()
        word.name = L[1].strip()
        word.tags = "Common;"
        word.part_of_speech = "N"
        word.save()
    f.close()
    print("Imported common nouns.")
    return

######################################
### Unused methods below this line ###
######################################

def read_from_file(file):    
    f = open(file, 'r')
    for line in f:
        params = line.split()
            
        word = Word()
        word.name = params[0]
        word.part_of_speech = params[1]
        word.tags = params[2]
        word.valuation = params[3]
            
        word.save()
            
    f.close()
    return

def basic_list():

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

    word5 = Word()
    word5.name = "zesty"
    word5.save()
    return