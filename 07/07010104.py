# 7.1.1.4 デコーディング
place = 'caf\u00e9'
place

type(place)

place_bytes = place.encode('utf-8')
place_bytes

type(place_bytes)

place2 = place_bytes.decode('utf-8')
place2

# 以下はエラー
# UTF-8でエンコードしたものをASCIIでデコードしているため
place3 = place_bytes.decode('ascii')
# 以下は文字化け
place4 = place_bytes.decode('latin-1')
# 以下は文字化け
place5 = place_bytes.decode('windows-1252')

