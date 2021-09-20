# unittest  https://docs.python.org/ja/3/library/unittest.html
# python test_example_01.py
# python test_example_01.py -v  詳細な出力

# 三つの文字列メソッドをテストするスクリプト
# 基本形

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

# python -m unittest test_module1 test_module2  モジュールを指定
# python -m unittest -v test_module 詳細を表示する
# python -m unittest test_module.TestClass  クラスを指定
# python -m unittest test_module.TestClass.test_method  メソッドを指定
# python -m unittest tests/test_something.py    ファイルパスで指定
