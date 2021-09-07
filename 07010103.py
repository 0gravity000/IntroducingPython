# 7.1.1.3 エンコーディング
snowman = '\u2603'

len(snowman)

ds = snowman.encode('utf-8')

len(ds)

ds

ds = snowman.encode('ascii')    # エラー UnicodeEncodeError

# 第2引数の指定がない場合は strict
# エンコードできないものは無視
snowman.encode('ascii', 'ignore')
# エンコードできないものは?に置き換え
snowman.encode('ascii', 'replace')
# unicode-escape形式のPython Unicode文字列を生成する
snowman.encode('ascii', 'backslashreplace')
# Webページで使えるエンティティの文字列を生成する
snowman.encode('ascii', 'xmlcharrefreplace')