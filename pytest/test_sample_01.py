# https://pytest.org/en/6.2.x/getting-started.html
# pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

# 複数のテストを実行する
# pytest現在のディレクトリとそのサブディレクトリで、
# test _*.py または *_test.py の形式のすべてのファイルを実行します。
