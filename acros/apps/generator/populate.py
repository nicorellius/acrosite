"""
file        :   populate.py
date        :   2014-11-24
module      :   generator
classes     :   
description :   Populate the database with Word models.
"""

from .models import Word
from .build_construction import len_valid_characters

def import_alpha_list():

    f = open("resources/condensed/complete_word_list_alpha.txt")
    counter = 0;

    for line in f:
        
        #for debugging - to identify the problem line (when parsing not working correctly)
        #print(line)
        
        if len(line) > 1:

            chars = list(line)

            if chars[0] != "#":

                params = line.split('\t')
            
                word = Word()
                
                # required arguments
                word.name = params[0]
                word.name_length = len_valid_characters(list(params[0]))
                word.part_of_speech = params[1]
                word.tags = params[2]
                word.save()

                counter += 1

    print("Constructed Word database with {0} Entries.".format(counter))        
    return


def alphabetize_and_replace_list(original_list, replacement_list_path):
    f = open(original_list)
    word_list = []
    comments_list = []
    for line in f:
        
        #for debugging - to identify the problem line (when parsing not working correctly)
        #print(line)
        
        if len(line) > 1:

            chars = list(line)

            if chars[0] != "#":

                params = line.split('\t')
                
                #sort tags list
                tags_list = params[2].strip().split(';')
                tags_list.sort()
                tags_sorted = ''
                for tag in tags_list:
                    if tag != '':
                        tags_sorted += tag + ';'

                line_entry = '{0}\t{1}\t{2}\n'.format(params[0],params[1],tags_sorted)
                word_list.append(line_entry)
            else:
                comments_list.append(line)
    f.close()
    
    #sorted alphabetically by word
    word_list.sort()
    
    #write to new file
    with open(replacement_list_path,'w') as f_out:
        for comment in comments_list:
            f_out.write(comment)
        
        for word_entry in word_list:
            if word_entry.strip() != '':
                f_out.write(word_entry)
    
    return
    
def all_subject_databases(theme_files):

    print("Importing all theme-specific files.")

    counter = 0
    
    for file in theme_files:
        print("Importing theme-specific word list: {0}.".format(file))
        counter += subject_database("resources/themes/{0}.txt".format(file), file)

    return counter


def subject_database(database_file, *args):

    f = open(database_file)
    theme_name = "none"

    if len(args) > 0:
        theme_name = args[0]
    
    counter = 0

    for line in f:

        if len(line) > 1:

            chars = list(line)

            if chars[0] != "#":

                params = line.split()
            
                word = Word()
                
                # required arguments
                word.name = params[0]
                word.part_of_speech = params[1]
                word.themes = theme_name
                
                # optional arguments
                if len(params) > 2:
                    word.tags = params[2]
                    
                    if len(params) > 3:
                        word.valuation = params[3]

                word.save()
                counter += 1
            
    f.close()

    print("Subject database {0} imported ({1} entries).".format(database_file, str(counter)))

    return counter


def populate_database(theme_files):

    counter = 0
    # counter += import_negative_adjectives()
    # counter += import_positive_adjectives()
    # counter += import_other_adjectives()
    # counter += import_common_nouns()
    # counter += import_common_infinitive_verbs()
    # counter += import_common_adverbs()
    # counter += import_pronouns()
    counter += all_subject_databases(theme_files)

    print("Successfully built a word database of {0} words.".format(str(counter)))
    
    return


def import_negative_adjectives():
    f = open("resources/general/top_100_negative_adjectives.txt")
    # https://www.englishclub.com/vocabulary/adjectives-personality-negative.htm
    
    counter = 0

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "common;negative;"
        word.part_of_speech = "A"
        word.themes = "cute_animals;music;politics"
        word.save()
        print('{0}\tA\tcute_animals;music;politics\tcommon;negative'.format(word.name));
        counter += 1

    f.close()

    print("Imported {0} negative adjectives.".format(str(counter)))

    return counter


def import_positive_adjectives():

    f = open("resources/general/top_100_positive_adjectives.txt")
    # https://www.englishclub.com/vocabulary/adjectives-personality-positive.htm
    
    counter = 0

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "common;positive;"
        word.part_of_speech = "A"
        word.themes = "cute_animals;music;politics"
        word.save()
        print('{0}\tA\tcute_animals;music;politics\tcommon;positive;'.format(word.name));
        counter += 1

    f.close()

    print("Imported {0} positive adjectives.".format(str(counter)))

    return counter


def import_other_adjectives():

    f = open("resources/general/other_adjectives.txt")
    # added by hand
    
    counter = 0

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Common;"
        word.part_of_speech = "A"
        word.themes = "all"
        word.save()
        counter += 1

    f.close()

    print("Imported {0} other adjective(s).".format(str(counter)))

    return counter


def import_common_nouns():

    f = open("resources/general/top_100_common_nouns.txt")
    # http://www.espressoenglish.net/100-common-nouns-in-english/
    
    counter = 0

    for line in f:
        word = Word()
        L = line.split()
        word.name = L[1].strip()
        word.tags = "Common;"
        word.part_of_speech = "NS"
        word.themes = "all"
        word.save()
        counter += 1

    f.close()

    print("Imported {0} common nouns.".format(str(counter)))

    return counter


def import_common_infinitive_verbs():

    f = open("resources/general/common_infinitive_verbs.txt")
    # http://www.enchantedlearning.com/wordlist/verbs.shtml
    

    counter = 0

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Common;"
        word.part_of_speech = "VP" # really, it's VS, but for now let's assume this for testing.
        word.themes = "all"
        word.save()
        counter += 1

    f.close()

    print("Imported {0} common infinitive verbs.".format(str(counter)))

    return counter


def import_common_adverbs():

    f = open("resources/general/common_adverbs.txt")
    # http://www.enchantedlearning.com/wordlist/adverbs.shtml
    
    counter = 0

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Common;"
        word.part_of_speech = "D"
        word.themes = "all"
        word.save()
        counter += 1

    f.close()

    print("Imported {0} common adverbs.".format(str(counter)))

    return counter


def import_pronouns():

    f = open("resources/general/pronouns.txt")
    # http://www.enchantedlearning.com/wordlist/adverbs.shtml
    
    counter = 0 

    for line in f:
        word = Word()
        word.name = line.strip()
        word.tags = "Common;"
        word.part_of_speech = "P"
        word.themes = "all"
        word.save()
        counter += 1

    f.close()

    print(("Imported {0} pronouns.".format(str(counter))))

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