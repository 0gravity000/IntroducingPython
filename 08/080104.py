# 8.1.4 read()によるバイナリファイルの読み出し
fin = open('bfile', 'rb')
bdata = fin.read()
len(bdata)

fin.close()