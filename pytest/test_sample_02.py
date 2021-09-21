# https://pytest.org/en/6.2.x/getting-started.html
# 特定の例外が発生したことを表明します
# pytest -q test_sample_02.py   「静かな」レポートモードでテスト機能を実行します。

import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
