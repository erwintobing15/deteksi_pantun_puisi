from django.test import TestCase
from detection.svm.classifier import get_poem_type

class DetectionTestCase(TestCase):

    def test_get_poem_type_return_empty_string_on_empty_parameter(self):
        """
        get_poem_type will return False when received empty parameter poem
        """
        poem = []
        poem_type = get_poem_type(poem)
        self.assertIs(poem_type, False)
