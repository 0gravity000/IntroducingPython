# 4.7.10 無名関数：ラムダ関数
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)

# ラムダ関数
edit_story(stairs, lambda word: word.capitalize() + '!')