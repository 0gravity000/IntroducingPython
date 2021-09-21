# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

# pip install -U pytest
# pytest

'''
=============================================== test session starts ================================================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: C:\as\v2\010_prg\040_python\IntroducingPython\pytest_documantation\01
collected 1 item

test_sample.py F                                                                                              [100%]

===================================================== FAILURES =====================================================
___________________________________________________ test_answer ____________________________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:6: AssertionError
============================================= short test summary info ==============================================
FAILED test_sample.py::test_answer - assert 4 == 5
================================================ 1 failed in 0.19s =================================================

[100％]は、すべてのテストケースの実行の全体的な進捗状況を示します。 終了後、pytestは失敗レポートを表示します
func（3）は5を返さないためです。

注：assertステートメントを使用して、テストの期待値を検証できます。 pytestの高度なアサーションイントロスペクションは
アサート式の中間値をインテリジェントにレポートするため、JUnitレガシーメソッドの多くの名前を回避できます。
'''