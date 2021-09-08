# 4.7.6 docstring
def echo(anything):
    'echoは与えられた入力引数を返す'
    return anything

def print_if_true(thing, check):
    '''
    第２引数が真なら、第１引数を表示する
    処理内容：
        1. *第２*引数が真かどうかチェックする
        2. 真なら*第１*引数を表示する
    '''
    if check:
        print(thing)

help(echo)

print(echo.__doc__)

print(print_if_true.__doc__)

