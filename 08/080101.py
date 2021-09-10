# 8.1.1 write()によるテキストファイルへの書き込み
poem = '''There was a young lady named Bright,
    Whose speed was far faster than light;
    She started one day
    In a relative way,
    And return on the previos night.'''
len(poem)

fout = open('./08/relativity', 'wt')
# write()でファイル書き込み
fout.write(poem)
fout.close()

fout = open('./08/relativity', 'wt')
# print()でファイル書き込みもできる
print(poem, file=fout)
fout.close()

# write()とprint()のどちらを使うべきか？
# print()の引数
#   sep セパレータ。デフォルトでスペース(' ')
#   end 末尾の文字列。デフォルトで改行('\n')

fout = open('./08/relativity', 'wt')
# print()の引数、sep, endを指定
print(poem, file=fout, sep='', end='')
fout.close()

# チャンクに分けて書き込みもできる
fout = open('./08/relativity', 'wt')
size = len(poem)
offset = 0
chank = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chank])
    offset += chank
fout.close()

# xモードを使うと、上書きを防げる
fout = open('./08/relativity', 'xt')

# 例外ハンドラとともに使うこともできる
try:
    fout = open('./08/relativity', 'xt')
    fout.write('stomp, stomp, stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')
    