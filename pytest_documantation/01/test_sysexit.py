# content of test_sysexit.py
import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

# Execute the test function with “quiet” reporting mode:
# 「静かな」レポートモードでテスト機能を実行します。
# pytest -q test_sysexit.py

'''
.                                                                                                             [100%]
1 passed in 0.06s

注：-q/--quietフラグは、この例と次の例で出力を簡潔に保ちます。

'''