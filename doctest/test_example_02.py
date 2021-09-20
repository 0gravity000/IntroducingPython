# python test_example_02.py  すべての実行例が正しく動作すると何も表示されない
# python test_example_02.py -v 詳細なログを出力
# python -m doctest -v test_example_02.py

import doctest
doctest.testfile("example_02.txt")

# testmod() と同じく、 testfile() は実行例が失敗しない限り何も表示しません
# https://docs.python.org/ja/3/library/doctest.html#doctest.testfile
