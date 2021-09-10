# 8.1.6 seek()による位置の変更
fin = open('./08/bfile', 'rb')
# tell()は現在のファイル先頭からのオフセットをバイト単位で返す
fin.tell()
# seek()はファイル内の別のオフセットへ移動する
# ファイルの末尾の1バイト手前に移動する
fin.seek(255)
# ファイルの末尾まで読み出す
bdata = fin.read()
len(bdata)
bdata[0]

# seek( offset, origin )
# origin = 0(デフォルト)    先頭からoffsetバイトの位置に移動する
# origin = 1    現在の位置からoffsetバイトの位置に移動する
# origin = 2    末尾からoffsetバイトの位置に移動する

fin = open('./08/bfile', 'rb')
# ファイルの末尾よりも1バイト手前に移動する
fin.seek(-1, 2)
fin.tell()
# ファイルの末尾まで読み出す
bdata = fin.read()
len(bdata)
bdata[0]

fin = open('./08/bfile', 'rb')
# ファイルの末尾よりも2バイト手前に移動する
fin.seek(254, 0)
fin.tell()
# ここから1バイト前進する
fin.seek(1, 1)
fin.tell()
# ファイルの末尾まで読み出す
bdata = fin.read()
len(bdata)
bdata[0]

fin.close()
