# 8.1.1 write()によるテキストファイルへの書き込み
poem = '''There was a young lady named Bright,
    Whose speed was far faster than light;
    She started one day
    In a return on the previos night.'''
len(poem)

fout = open('relativity', 'wt')
fout.write(poem)

fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chank = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chank])
    offset += chank

fout.close()

#
fout = open('relativity', 'xt')

#
try:
    fout = open('relativity', 'wt')
    fout.write('stomp, stomp, stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')