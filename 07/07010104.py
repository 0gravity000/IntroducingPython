# 7.1.1.4 デコーディング
# バイト列（バイナリデータ）をデコードして文字列（テキストデータ）にする

# 何らかの外部ソース（ファイル、データベース、Webサイト、APIなど）から
# テキストを取り出した時、そのテキストはエンコードされたものである
# 難しいのは、実際にどのエンコーディングが使われているかを知ることである
# それがわからなけれは、エンコードの逆のデコードで文字列が得られない
# しかし、バイト列自体のなかに、どのエンコーディングが使われているかを教えてくれるものはない

# Unocode文字列を作る
place = 'caf\u00e9'
place
type(place) #str

# UTF-8でエンコードする
place_bytes = place.encode('utf-8')
place_bytes
type(place_bytes) #byte
len(place_bytes)  #5バイト。最初の3バイトはASCIIと同じで、最後の2バイトがéをエンコードしている

# バイト列をUnicode文字列にデコード
place2 = place_bytes.decode('utf-8')
place2

# 以下はエラー
# UTF-8でエンコードしたものをASCIIでデコードしているため
place3 = place_bytes.decode('ascii')
# 以下は文字化け
place4 = place_bytes.decode('latin-1')
# 以下は文字化け
place5 = place_bytes.decode('windows-1252')

# 可能な限りUTF-8エンコーディングを使うこと
