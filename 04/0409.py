# 4.9 デコレータ
# デコレータは入力として関数をひとつ取り、別の関数を返す関数

# デコレータを定義
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

#
def add_ints(a, b):
    return a + b

add_ints(3, 5)

cooler_add_ints = document_it(add_ints) #手作業でデコレータの戻り値を代入
cooler_add_ints(3, 5)

# デコレートしたい関数の直前に、@decorator_nameを追加する
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
'''
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8
'''


# 別のデコレータを定義
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

# 複数のデコレータを実行
@document_it
@square_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
'''
Running function: new_function
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 64
64
'''

#
@square_it
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
'''
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
64
'''