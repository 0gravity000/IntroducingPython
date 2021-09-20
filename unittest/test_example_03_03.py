# unittest  https://docs.python.org/ja/3/library/unittest.html
# python test_example_03_03.py
# python test_example_03_03.py -v  詳細な出力
# テストのスキップと予期された失敗 (expected failure)

import unittest

# 予期された失敗の機能を使用するには expectedFailure() デコレータを使います。
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
