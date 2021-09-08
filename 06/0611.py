# 6.11 ダックタイピング

# 親クラス
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

# 子クラス
class QuestionQuote(Quote):
    def says(self): #says()メソッドをオーバーライド
        return self.words + '?'

# 子クラス
class ExclamationQuote(Quote):
    def says(self): #says()メソッドをオーバーライド
        return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

# 異なる3種類のsays()メソッドが3つのクラスのために異なる動作をする
# これがオブジェクト指向言語の店頭的なポリモーフィズム
# who()、says()メソッドを持ちさえすれば、どのようなオブジェクトであっても
# 継承などを利用しなくても、
# 共通のインターフェイスを持つオブジェクトとして扱うことができる

class BabblingBrook():
    def who(self):
        return 'Brook'
    def seys(self):
        return 'Babble'

brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
# これは、他とまったく無関係
who_says(brook)

# このような動作は古いことわざにちなんでダックタイピングと呼ばれる
# アヒルのように歩き、アヒルのようにクワッと鳴くなら、それはアヒルだ
