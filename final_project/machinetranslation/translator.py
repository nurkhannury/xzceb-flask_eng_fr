"""
This module provides translation functions using MyMemoryTranslator.
"""

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
