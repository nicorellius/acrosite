from django.test import TestCase

from acrosite.acros.apps.generator.models import Word

# Create your tests here.
class WordMethodTests(TestCase):
    def word_exists(self):
        w = Word('hello')
        self.assertEqual(False, False)