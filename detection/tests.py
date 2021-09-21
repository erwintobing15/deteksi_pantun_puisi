from django.test import TestCase
from detection.svm.classifier import get_poem_type, get_poem_probability

class DetectionTestCase(TestCase):

    def test_get_poem_type_return_false_on_empty_parameter(self):
        """
        get_poem_type will return False when received empty parameter poem
        """
        poem = []
        poem_type = get_poem_type(poem)
        self.assertIs(poem_type, False)

    def test_get_poem_probability_return_false_on_empty_parameter(self):
        """
        get_poem_probability return False when received empty parameter poem
        """
        poem = []
        poem_type = get_poem_probability(poem)
        self.assertIs(poem_type, False)
