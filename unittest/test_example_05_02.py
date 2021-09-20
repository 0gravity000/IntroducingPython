
# test_sample.py テストをする側のコード
# python -m unittest test_example_05_02.TestStringMethods1
# python test_example_05_02.py
# python test_example_05_02.py -v  詳細な出力

import unittest
import example_05 as sample

class TestStringMethods1(unittest.TestCase):
 
    def setUpClass():
        print('*** 全体前処理 ***')
 
    def tearDownClass():
        print('*** 全体後処理 ***')
 
    def setUp(self):
        print('+ テスト前処理')
 
    def tearDown(self):
        print('+ テスト後処理')
 
    def test_add_num(self):
        """ 
        add_numの単体テスト
        """
        print("test_add_num開始")
        self.assertEqual(7, sample.add_num(3, 4)) 
        print("test_add_num終了")
 
    def test_is_positive(self):
        """
        is_numの単体テスト
        """
        print("test_is_positive開始")
        self.assertTrue(sample.is_positive(3))
        self.assertFalse(sample.is_positive(0))
        self.assertFalse(sample.is_positive(-1))
        print("test_is_positive終了")

if __name__ == '__main__':
    unittest.main()
