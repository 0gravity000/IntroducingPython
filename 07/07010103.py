# 7.1.1.3 エンコーディング
# 文字列（テキストデータ）をエンコードしてバイト列（バイナリデータ）にする

# encode()の第1引数はエンコーディンク名
# 'ascii' 古き良き7ビットASCII
# 'utf-8' 8ビット可変長エンコーディング。ほぼこれを使う
# 'latin-1' ISO 8859-1と呼ばれるもの
# 'cp-1252' 一般的なWindowsエンコーディング
# 'unicode-escape'  Python Unicodeリテラル形式。\uxxxx、\Uxxxxxxxx

# Unicode文字列を代入
snowman = '\u2603'
# Python内部に格納するのに何バイトかかったかにかかわらず、1文字のPython Unicode文字列
len(snowman)

# Unicode文字列をバイト列にutf-8エンコードする
ds = snowman.encode('utf-8')
# UTF-8は可変長エンコーディングなので、この場合1つの文字のエンコードに3バイト使っている
len(ds)
# エンコードされたバイト列
ds
# ASCIIの場合、エンコードエラー　snowmanはASCII変換できない
ds = snowman.encode('ascii')

# encode()の第2引数
# 第2引数の指定がない場合は strict
# エンコードできないものは無視
snowman.encode('ascii', 'ignore')
# エンコードできないものは?に置き換え
snowman.encode('ascii', 'replace')
# unicode-escape形式のPython Unicode文字列を生成する
snowman.encode('ascii', 'backslashreplace')
# Webページで使えるエンティティの文字列を生成する
snowman.encode('ascii', 'xmlcharrefreplace')
