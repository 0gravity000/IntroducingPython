# unittest  https://docs.python.org/ja/3/library/unittest.html
# python test_example_03_02.py
# python test_example_03_02.py -v  詳細な出力
# テストのスキップと予期された失敗 (expected failure)

import unittest

# テストクラスは以下のようにメソッドをスキップすることができます:
# TestCase.setUp() もスキップすることができます。
# この機能はセットアップの対象のリソースが使用不可能な時に便利です。
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
