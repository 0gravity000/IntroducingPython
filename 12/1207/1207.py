# 12.7 Pythonコードのデバッグ
# デバックでもっとも単純なのは、文字列を表示すること
# vars()は、関数への引数を含むローカル変数の値を抽出する
def func(*args, **kwargs):
  print(vars())

func(1, 2, 3)
func(['a', 'b', 'argh'])
