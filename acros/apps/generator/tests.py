"""
file         :   tests.py
date         :   2014-11-06
module       :   generator
classes      :   WordExistsTest
description  :   tests for generator application
"""

from django.test import TestCase

from .models import Word
from . import magic


class WordExistsTestCase(TestCase):
    
    def setUp(self):
        
        Word.objects.create(name='hello')
        Word.objects.create(name='goodbye')
        
    
    def test_word_exists(self):
        
        hello = Word.objects.get(name="hello")
        goodbye = Word.objects.get(name="goodbye")
        
        self.assertEqual(hello.name, 'hello')
        self.assertEqual(goodbye.name, 'goodbye')
        
        
class WordMagicTest(TestCase):

    def test(self):
        
        self.assertEqual(magic.first_letter("Abracadabra"), "A")
        
        self.assertEqual(magic.get_format("So happy it's Thursday"), ['IN', 'JJ', 'PRP', 'VBZ', 'NNP'])
        
        self.assertEqual(magic.get_format("Thank God it's Friday"), ['NNP', 'NNP', 'PRP', 'VBZ', 'NNP'])
        
        self.assertEqual(
            magic.get_format("We're always cuddling koala's yearly"),
            ['PRP', 'VBP', 'RB', 'VBG', 'NN', 'POS', 'JJ'])
        
        #self.assertEqual(get_formats('sample'),'sample')