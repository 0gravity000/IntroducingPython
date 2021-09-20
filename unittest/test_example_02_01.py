# unittest  https://docs.python.org/ja/3/library/unittest.html
# python test_example_02_01.py
# python test_example_02_01.py -v  詳細な出力

import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))
