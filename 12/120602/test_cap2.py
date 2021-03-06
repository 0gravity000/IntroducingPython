import unittest
import cap2

class TestCap2(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_word(self):
        text = 'duck'
        result = cap2.just_do_it(text)
        self.assertEqual(result, 'Duck')

    def test_multiple_words(self):
        text = 'a varitable flock of ducks'
        result = cap2.just_do_it(text)
        self.assertEqual(result, 'A Varitable Flock Of Ducks')

if __name__ == '__main__':
    unittest.main()