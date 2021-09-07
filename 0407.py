# 4.7 関数
# 何もしない関数の定義
def do_nothing():
    pass

# 何もしない関数の呼び出し
do_nothing()

#
def make_a_sound():
    print('quack')

make_a_sound()

#
def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected')

#
def echo(anything): # anything は仮引数
    return anything + ' ' + anything

echo('foo') # foo は実引数

#
def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."
    
comment = commentary('blue')
print(comment)

#
print(do_nothing())