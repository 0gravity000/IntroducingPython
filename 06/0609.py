# 6.9 非公開属性のための名前のマングリング
# Pythonは、クラス定義の外からが見えないようにすべき属性の命名方法を持っている
# 先頭にふたつのアンダースコア__を付ける
class Duck():
    def __init__(self, input_name):
        self.__name = input_name    #外からアクセスできないプロパティ
    @property
    def name(self): #ゲッター
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name): #セッター
        print('inside the setter')
        self.__name = input_name

# オブジェクト(インスタンス)を作る
fowl = Duck('Howard')
# ゲッター
fowl.name
# inside the getter
# 'Howard'

# セッター
fowl.name = 'Donald'
# inside the setter

fowl.name
# inside the getter
# 'Donald'

# __name属性にはアクセスできない
fowl.__name     # エラー
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Duck' object has no attribute '__name'
'''

# これだとアクセスできる
fowl._Duck__name
# 'Donald'