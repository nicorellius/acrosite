import unittest
import operator
import nltk

"""
Note here the use of relative imports. This is best practices in Django.
They only work inside modules. Cross module imports require full path.
"""
from .models import Word


def first_letter(word):
    return word[0]


def get_formats(word):
    
    """
    Uses word length to determine useful pos structure.
    For example, given the word 'Fun', returns a list
    of three parts of speech because 'Fun' has three letters or
    several lists should they be available.
    :param word: Use word length
    :return: A set of parts of speech structures
    """

    print(word)

    old_question = Word(word)

    print(old_question.word)
        
    # todo
    # check one-many mapping of word length to formats and return set of formats
    # we could also return formats of size -+2 to account for word contractions
    return []
    
def rank_formats(formats):
    
    """
    Given a set of formats, this ranks them returning a
    new mapping of the formats keyed by rank.
    :param formats: A set of pos formats
    :return: A mapping of those formats keyed and grouped by rank
    """
    # todo
    return {}

    
def get_word(format_element, knowledge):
    return None


def update(acrostic, knowledge):

    # knowledge + more info + current state of acrostic
    return knowledge


def money_maker(word, theme):

    """
    Given a word,
    1. determine it's formats
    2. for each format
    map each pos element and theme to retrieve a word
    update
    3. rank each format
    3. give the word with the best format score
    Use Markov chains -- http://en.wikipedia.org/wiki/Parody_generator
    :param word: A word
    :return: An awesome phrase
    """

    candidates = {}
    
    knowledge = {}

    for key, value in rank_formats(get_formats(word)):
        
        # knowledge.self(key, theme)
        acrostic = []
        
        for format_element in value:
            
            word = get_word(format_element, knowledge)
    
            update(acrostic, knowledge)
    
            acrostic.append(word)
    
            candidates[acrostic] = knowledge
    
    return max(candidates.iteritems(), key=operator.itemgetter(1))[0]


def get_format(acrostic):

    """
    Given an acrostic or phrase string, this function will
    return a list of the nltk tags which consist of the basic
    parts of speech and other nltk specific tags that are useful
    in the nltk universe.
    :param acrostic: An acrostic or phrase string
    :return: A list of nltk tags for each word
    """
    
    tokens = nltk.word_tokenize(acrostic)
    
    return [element[1] for element in nltk.pos_tag(tokens)]


class WordMagicTest(unittest.TestCase):

    def test(self):
        
        self.assertEqual(first_letter("Abracadabra"), "A")
        
        self.assertEqual(get_format("So happy it's Thursday"), ['IN', 'JJ', 'PRP', 'VBZ', 'NNP'])
        
        self.assertEqual(get_format("Thank God it's Friday"), ['NNP', 'NNP', 'PRP', 'VBZ', 'NNP'])
        
        self.assertEqual(
            get_format("We're always cuddling koala's yearly"),
            ['PRP', 'VBP', 'RB', 'VBG', 'NN', 'POS', 'JJ'])
        
        self.assertEqual(get_formats('sample'),'sample')