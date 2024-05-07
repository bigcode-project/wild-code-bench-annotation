import re
import string
from nltk.stem import PorterStemmer
from collections import Counter

STEMMER = PorterStemmer()

def f_169(content):
    """
    Stem every word in a sentence, except the last, and count the frequency of each stem.

    Parameters:
    content (str): The sentence to stem and count.

    Returns:
    dict: A dictionary with stemmed words as keys and their frequency as values.

    Requirements:
    - re
    - string
    - nltk.stem
    - collections.Counter

    Example:
    >>> f_169('running runner run')
    {'run': 1, 'runner': 1}
    """
    content = content.split(' ')[:-1]
    words = [word.strip(string.punctuation).lower() for word in re.split('\W+', ' '.join(content))]
    stemmed_words = [STEMMER.stem(word) for word in words]
    word_counts = Counter(stemmed_words)
    return dict(word_counts)

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_169('running runner run')
        self.assertEqual(result, {'run': 1, 'runner': 1})
    
    def test_case_2(self):
        result = f_169('dancing dancer danced')
        self.assertEqual(result, {'danc': 1, 'dancer': 1})
        
    def test_case_3(self):
        result = f_169('loving lover love')
        self.assertEqual(result, {'love': 1, 'lover': 1})
        
    def test_case_4(self):
        result = f_169('computing computer compute')
        self.assertEqual(result, {'comput': 2})
        
    def test_case_5(self):
        result = f_169('swimming swimmer swim')
        self.assertEqual(result, {'swim': 1, 'swimmer': 1})