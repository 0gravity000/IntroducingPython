# unittest  https://docs.python.org/ja/3/library/unittest.html
# python test_example_04_01.py
# python test_example_04_01.py -v  詳細な出力
# サブテストを利用して繰り返しテストの区別を付ける

import unittest

class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

if __name__ == '__main__':
    unittest.main()
