# 5.3.4 モジュールサーチパス
import sys
for place in sys.path:
    print(place)

'''
sys.path変数に格納されているディレクトリ
結果

C:\Users\0grav\AppData\Local\Programs\Python\Python39\python39.zip
C:\Users\0grav\AppData\Local\Programs\Python\Python39\DLLs
C:\Users\0grav\AppData\Local\Programs\Python\Python39\lib
C:\Users\0grav\AppData\Local\Programs\Python\Python39
C:\Users\0grav\AppData\Local\Programs\Python\Python39\lib\site-packages

最初の空行は空文字''でカレントディレクトリという意味

Pythonはimportするファイルを探す時、
Pythonは、まずカレントディレクトリを見る
その後、上記の箇所を探す

つまり、自分でrandomというモジュールを定義すると、
標準ライブラリのrandomにアクセスできなくなる

'''
