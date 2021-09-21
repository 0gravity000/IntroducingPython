class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

# pytest -q test_class.py

'''
pytestは、Pythonテスト検出の規則に従ってすべてのテストを検出するため、test_プレフィックス付きの両方の関数を検出します。
何もサブクラス化する必要はありませんが、クラスの前にTestを付けるようにしてください。
そうしないと、クラスがスキップされます。 ファイル名を渡すだけでモジュールを実行できます。

pytest -q test_class.py

.F                                                                                                            [100%]
===================================================== FAILURES =====================================================
________________________________________________ TestClass.test_two ________________________________________________

self = <test_class.TestClass object at 0x0000015C87FC9A00>

    def test_two(self):
        x = "hello"
>       assert hasattr(x, "check")
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_class.py:8: AssertionError
============================================= short test summary info ==============================================
FAILED test_class.py::TestClass::test_two - AssertionError: assert False
1 failed, 1 passed in 0.12s

最初のテストは合格し、2番目のテストは失敗しました。 
アサーションの中間値を簡単に確認して、失敗の理由を理解するのに役立てることができます。
クラスでのテストのグループ化は、次の理由で有益な場合があります。
•テスト組織
•その特定のクラスでのみテスト用のフィクスチャを共有する
•クラスレベルでマークを適用し、それらをすべてのテストに暗黙的に適用させる
クラス内でテストをグループ化するときに注意する必要があるのは、各テストにはクラスの一意のインスタンスがあるということです。
各テストが同じクラスインスタンスを共有することは、テストの分離に非常に有害であり、不十分なテストプラクティスを促進します。 
これは以下に概説されています：
# content of test_class_demo.py


'''