# 8.1.3 write()によるバイナリファイルの書き込み
bdata = bytes(range(0, 256))
len(bdata)

fout = open('./08/bfile', 'wb')
fout.write(bdata)
fout.close

# チャンクを指定して書き込みできる
fout = open('./08/bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk
fout.close