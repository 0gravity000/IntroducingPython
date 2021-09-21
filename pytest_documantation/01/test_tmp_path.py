# content of test_tmp_path.py
def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0

'''
pytest -q test_tmp_path.py

F                                                                                                             [100%]
===================================================== FAILURES =====================================================
_________________________________________________ test_needsfiles __________________________________________________

tmp_path = WindowsPath('C:/Users/0grav/AppData/Local/Temp/pytest-of-0grav/pytest-0/test_needsfiles0')

    def test_needsfiles(tmp_path):
        print(tmp_path)
>       assert 0
E       assert 0

test_tmp_path.py:4: AssertionError
----------------------------------------------- Captured stdout call -----------------------------------------------
C:\Users\0grav\AppData\Local\Temp\pytest-of-0grav\pytest-0\test_needsfiles0
============================================= short test summary info ==============================================
FAILED test_tmp_path.py::test_needsfiles - assert 0
1 failed in 0.20s

一時ディレクトリの処理の詳細については、一時ディレクトリとファイルを参照してください。
2.6 How to use temporary directories and files in tests
2.6.1 The tmp_path fixture

次のコマンドを使用して、どのような種類の組み込みpytestフィクスチャが存在するかを確認します。
pytest --fixtures # shows builtin and custom fixtures

このコマンドでは、-vオプションが追加されていない限り、先頭に__が付いたフィクスチャが省略されることに注意してください。

'''
