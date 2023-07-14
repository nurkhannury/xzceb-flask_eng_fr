import unittest
import os
import sys


from deep_translator import MyMemoryTranslator

translator = MyMemoryTranslator(source='en-US', target='fr-FR')

def english_to_french(english_text):
    """
    Translates English text to French using MyMemoryTranslator.
    :param english_text: English text to translate.
    :return: Translated French text.
    """
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using MyMemoryTranslator.
    :param french_text: French text to translate.
    :return: Translated English text.
    """
    english_text = translator.translate(french_text, source='fr-FR', target='en-US')
    return english_text

class TranslationTests(unittest.TestCase):
    def test_english_to_french_hello(self):
        translation = english_to_french('Hello')
        self.assertEqual(translation, 'Bonjour')

    def test_french_to_english_bonjour(self):
        translation = french_to_english('Bonjour')
        self.assertEqual(translation, 'Hello')

    def test_english_to_french_other_word(self):
        translation = english_to_french('Goodbye')
        self.assertEqual(translation, 'Au revoir')

    def test_french_to_english_other_word(self):
        translation = french_to_english('Merci')
        self.assertEqual(translation, 'Thank you')

if __name__ == '__main__':
    unittest.main()
