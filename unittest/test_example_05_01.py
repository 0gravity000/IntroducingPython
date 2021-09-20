
# test_sample.py テストをする側のコード
# python -m unittest test_example_05_01.TestStringMethods1
# python test_example_05_01.py
# python test_example_05_01.py -v  詳細な出力

import unittest
import example_05 as sample
 
class TestStringMethods1(unittest.TestCase):
 
    def test_add_num(self):
        """ 
        add_numの単体テスト
        """
        self.assertEqual(7, sample.add_num(3, 4)) 
 
    def test_is_positive(self):
        """
        is_numの単体テスト
        """
        self.assertTrue(sample.is_positive(3))
        self.assertFalse(sample.is_positive(0))
        self.assertFalse(sample.is_positive(-1))

if __name__ == '__main__':
    unittest.main()
