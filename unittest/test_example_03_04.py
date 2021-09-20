# unittest  https://docs.python.org/ja/3/library/unittest.html
# python test_example_03_04.py
# python test_example_03_04.py -v  詳細な出力
# テストのスキップと予期された失敗 (expected failure)

import unittest

# 独自のスキップ用のデコレータの作成
# 独自のデコレータのスキップしたい時点で skip() を呼び出します。 
# 以下のデコレータはオブジェクトに指定した属性が無い場合にテストをスキップします:
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))
