# 8.5.3 Redis
# Redisはデータ構造サーバー
# pip install redis
# Redisサーバーのインストールも必要
# https://weblabo.oscasierra.net/redis-windows-install/

# 8.5.3.1 文字列

# Redisをインポート
import redis
# Redisサーバーに接続
# redis.Redis('localhost')、redis.Redis('localhost', '6379')でもOK
conn = redis.Redis()
# すべてのキーのリストを表示する（今のところキーはない）
conn.keys('*')
# キーと値を書き込む
conn.set('secret', 'ni!')
conn.set('carats', 24)
conn.set('fever', '101.5')
# キーを使って値を読み出す
conn.get('secret')
conn.get('carats')
conn.get('fever')

# キーが存在しないときに限り、値を設定する。これは設定失敗する
conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')
# すでに secret は存在するため
conn.get('secret')
# getset()はもともとの値を返すとともに、新しい値を設定する
conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!')
conn.get('secret')
# getrange()は部分文字を取り出す
conn.getrange('secret', -6, -1)
# setrange()は部分文字列を置換する
conn.setrange('secret', 0, 'ICKY')
conn.get('secret')
# mset()は同時に複数のキーを設定する
conn.mset({'pie': 'cherry', 'cordial': 'sherry'})
# mget()は一度に複数の値が得られる
conn.mget(['fever', 'carats'])
# delete()はキーを削除する
conn.delete('fever')
# incr()、incrbyfloat()はインクリメントし、decr()はデクリメントする
conn.incr('carats')
conn.incr('carats', 10)
conn.decr('carats')
conn.decr('carats', 15)
conn.set('fever', '101.5')
conn.incrbyfloat('fever')
conn.incrbyfloat('fever', 0.5)
# decrbyfloat()はない。マイナス値を指定する
conn.incrbyfloat('fever', -2.0)
