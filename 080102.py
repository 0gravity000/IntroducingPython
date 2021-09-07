# 8.1.2 read()、readline()、readlines()によるテキストファイルの読み出し
fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
chank = 100
while True:
    fragment = fin.read(chank)
    if not fragment:
        break
    poem += fragment
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
len(poem)


oem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
fin.close()
len(poem)

oem = ''
fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')

for line in lines:
    print(line, end='')