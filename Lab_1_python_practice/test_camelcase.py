import camelcase

from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('displayAllBooks', camelcase.camelcase('Display all books'))
        
    def test_camelcase_empty_string(self):

        self.assertEqual('', camelcase.camelcase(''))

    def test_camelcase_one_word(self):

        self.assertEqual('hello', camelcase.camelcase('hello'))

    def test_camelcase_upper_lower_mix(self):

        self.assertEqual('helloWorld', camelcase.camelcase('hElLo wOrLd'))

    def test_camelcase_leading_trailing_spaces(self):

        self.assertEqual('helloWorld', camelcase.camelcase('  hello world  '))

    def test_camelcase_strings_with_numbers(self):

        self.assertEqual('version2Update', camelcase.camelcase('version 2 update'))

    def test_camel_case_unicode_characters(self):

        self.assertEqual('caféMañana', camelcase.camelcase('café mañana'))
    
    def test_camelcase_emojis(self):

        self.assertEqual('helloWorld😊', camelcase.camelcase('hello world😊'))

    def test_camelcase_newline(self):

        self.assertEqual('helloWorld', camelcase.camelcase('hello\nworld\t'))
        