# unittest  https://docs.python.org/ja/3/library/unittest.html
# python test_example_02_04.py
# python test_example_02_04.py -v  詳細な出力
# テストスイート

import unittest
from test_example_02_03 import WidgetTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
