# 6.2 classによるクラス定義
# 空クラス。passはクラスが空だということを示す
class Person():
    pass

# Personクラスからsomeoneオブジェクト(インスタンス)を作る
someone = Person()

# Pythonオブジェクトを初期化する特殊メソッド__init__
# __init__()は、クラス定義から個々のオブジェクトを作るときに、それを初期化するメソッド
# self引数は、作られたオブジェクト自体を参照することを示す
# __init__()の第1引数はselfでなければならない
# __init__()は、同じクラスから作られた、他のオブジェクトから
# このオブジェクトを区別するために必要な処理をするために使われる
class Person():
    def __init__(self):
        pass

# __init__()の第2引数にnameを追加

class Person():
    def __init__(self, name):
        self.name = name

# hunterオブジェクト(インスタンス)を作成
hunter = Person('Elmer Fudd')
print('The mighty hunter: ', hunter.name)
