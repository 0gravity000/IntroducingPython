# unittest  https://docs.python.org/ja/3/library/unittest.html
# python test_example_02_03.py
# python test_example_02_03.py -v  詳細な出力
# tearDown()

import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
