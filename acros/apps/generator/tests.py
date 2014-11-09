"""
file         :   tests.py
date         :   2014-11-06
module       :   generator
classes      :   WordExistsTest
description  :   tests for generator application
"""

from django.test import TestCase

from .models import Word



class WordExistsTestCase(TestCase):
    
    def setUp(self):
        
        Word.objects.create(name='hello')
        Word.objects.create(name='goodbye')
        
    
    def test_word_exists(self):
        
        hello = Word.objects.get(name="hello")
        goodbye = Word.objects.get(name="goodbye")
        
        self.assertEqual(hello.name, 'hello')
        self.assertEqual(goodbye.name, 'goodbye')