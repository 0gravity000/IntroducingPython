# 8.1.2 read()、readline()、readlines()によるテキストファイルの読み出し
# 大きなファイルを読み出すときは注意
# 1GBのファイルは1GBのメモリを消費する

fin = open('./08/relativity', 'rt')
poem = fin.read()
fin.close()
len(poem)

# チャンクを指定して読み出し
poem = ''
fin = open('./08/relativity', 'rt')
chank = 100
while True:
    fragment = fin.read(chank)
    if not fragment:
        break
    poem += fragment
fin.close()
len(poem)

# ファイルを1行づつ読み出す
poem = ''
fin = open('./08/relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
len(poem)

# イテレータを使ってファイルを1行づつ読み出す
oem = ''
fin = open('./08/relativity', 'rt')
for line in fin:
    poem += line
fin.close()
len(poem)

# 1度に1行ずつ読み出して、1行文字列のリストを返す
oem = ''
fin = open('./08/relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')