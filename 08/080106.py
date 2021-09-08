# 8.1.6 seek()による位置の変更
fin = open('bfile', 'rb')
fin.tell()

fin.seek(255)

bdata = fin.read()
len(bdata)

bdata[0]

# seek( offset, origin )
# origin = 0(デフォルト)    先頭からoffsetバイトの位置に移動する
# origin = 1    現在の位置からoffsetバイトの位置に移動する
# origin = 2    末尾からoffsetバイトの位置に移動する

fin = open('bfile', 'rb')
fin.seek(-1, 2)

fin.tell()

bdata = fin.read()
len(bdata)

bdata[0]