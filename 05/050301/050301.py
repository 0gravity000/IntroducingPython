# 5.3 モジュールとimport文
# 5.3.1 モジュールのインポート
'''
import文のもっとも単純な使い方
import モジュール

モジュールは、ファイル名から拡張子.pyを取り除いたもの
'''

# weatherman.py
import report   #reportモジュール全体をインポート

description = report.get_description()
print("Today's weather:", description)

# report.py
def get_description():
    """プロと同じようにランダムな天気を返す"""
    from random import choice   #randomモジュールのchoice()関数をインポート
    possibilies = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilies)

# report.py の別の書き方
def get_description():
    """プロと同じようにランダムな天気を返す"""
    import random   #random全体をインポート
    possibilies = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return random.choice(possibilies)

# importの呼び出し場所
# importされるコードが複数の場所で使われる場合、関数の外でインポートする
# 使われる場所が限定されている場合は、使う関数の中で呼び出す
import random   #random全体をインポート
def get_description():
    """プロと同じようにランダムな天気を返す"""
    possibilies = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return random.choice(possibilies)

# 実行
# python weatherman.py
# python weatherman.py
# python weatherman.py

