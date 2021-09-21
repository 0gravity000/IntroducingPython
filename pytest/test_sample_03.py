# https://pytest.org/en/6.2.x/getting-started.html
# 1つのクラスに複数のテストをグループ化する
# pytest -q test_sample_03.py   「静かな」レポートモードでテスト機能を実行します。

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
