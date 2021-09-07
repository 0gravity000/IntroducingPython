import cap2
from nose.tools import eq__ #??? importできない

def test_one_word():
    text = 'duck'
    result = cap2.just_do_it(text)
    eq__(result, 'Duck')

def test_multiple_words(self):
    text = 'a varitable flock of ducks'
    result = cap2.just_do_it(text)
    eq__(result, 'A Varitable Flock Of Ducks')

def test_words_with_apostrophes(self):
    text = "I'm fresh out of ideas"
    result = cap2.just_do_it(text)
    eq__(result, "I'm Fresh Out Of Ideas")

def test_words_with_quotes(self):
    text = "\"You're despicable,\" said Daffy Duck"
    result = cap2.just_do_it(text)
    eq__(result, "\"You're Despicable,\" Said Daffy Duck")
