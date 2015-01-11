"""
file        :   populate.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   Populate the database with Word models.
"""

from .models import Word


def subject_database(database_file):

    f = open(database_file)

    counter = 0

    for line in f:

        if len(line) > 1:

            chars = list(line)

            if chars[0] != "#":

                params = line.split()
            
                word = Word()
                
                #Required arguments
                word.name = params[0]
                word.part_of_speech = params[1]
                
                #Optional arguments
                if (len(params) > 2):
                    word.tags = params[2]
                    
                    if (len(params) > 3):
                        word.valuation = params[3]

                word.save()

                counter += 1
            
    f.close()

    print("Subject database {0} imported  ({1} entries).".format(database_file, str(counter)))

    return


def populate_database():

    counter = 0
    counter += import_negative_adjectives()
    counter += import_positive_adjectives()
    counter += import_other_adjectives()
    counter += import_common_nouns()
    counter += import_common_infinitive_verbs()
    counter += import_common_adverbs()
    counter += import_pronouns()

    print("Successfully built a word database of {0} words.".format(str(counter)))
    
    return


def import_negative_adjectives():
    f = open("resources/top_100_negative_adjectives.txt")
    # https://www.englishclub.com/vocabulary/adjectives-personality-negative.htm
    
    counter = 0

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Common;Negative;"
        word.part_of_speech = "A"
        word.save()
        counter += 1

    f.close()

    print("Imported {0} negative adjectives.".format(str(counter)))

    return counter


def import_positive_adjectives():

    f = open("resources/top_100_positive_adjectives.txt")
    # https://www.englishclub.com/vocabulary/adjectives-personality-positive.htm
    
    counter = 0

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Common;Positive;"
        word.part_of_speech = "A"
        word.save()
        counter += 1

    f.close()

    print("Imported {0} positive adjectives.".format(str(counter)))

    return counter


def import_other_adjectives():
    f = open("resources/other_adjectives.txt")
    # added by hand
    
    counter = 0

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Common;"
        word.part_of_speech = "A"
        word.save()
        counter += 1

    f.close()

    print("Imported {0} other adjectives.".format(str(counter)))

    return counter


def import_common_nouns():

    f = open("resources/top_100_common_nouns.txt")
    # http://www.espressoenglish.net/100-common-nouns-in-english/
    
    counter = 0

    for line in f:
        word = Word()
        L = line.split()
        word.name = L[1].strip()
        word.tags = "Common;"
        word.part_of_speech = "N"
        word.save()
        counter += 1

    f.close()

    print("Imported {0} common nouns.".format(str(counter)))

    return counter


def import_common_infinitive_verbs():

    f = open("resources/common_infinitive_verbs.txt")
    # http://www.enchantedlearning.com/wordlist/verbs.shtml
    

    counter = 0

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Common;"
        word.part_of_speech = "VI"
        word.save()
        counter += 1

    f.close()

    print("Imported {0} common infinitive verbs.".format(str(counter)))

    return counter


def import_common_adverbs():

    f = open("resources/common_adverbs.txt")
    # http://www.enchantedlearning.com/wordlist/adverbs.shtml
    
    counter = 0

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Common;"
        word.part_of_speech = "D"
        word.save()
        counter += 1

    f.close()

    print(("Imported " + str(counter) + " common adverbs."))

    return counter


def import_pronouns():

    f = open("resources/pronouns.txt")
    # http://www.enchantedlearning.com/wordlist/adverbs.shtml
    
    counter = 0 

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Common;"
        word.part_of_speech = "P"
        word.save()
        counter += 1

    f.close()

    print(("Imported " + str(counter) + " pronouns."))

    return counter


"""
Unused methods below this line
"""


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
    word3.themes = "insects;gross"
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