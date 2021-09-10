# 8.5.2 memcached
# memcachedは、キーと値のための高速なメインメモリのキャッシュサーバー
# データベースの前よりとして使用されたり
# ウェブサーバーのセッションデータの格納に使われたりすることが多い
# 動作させるには、memocachedサーバーとPythonドライバーが必要
# pip install python-memocached

import memcache
db = memcache.Client(['127.0.0.1:11211'])
db.set('macro', 'polo')

db.get('macro')

db.set('ducks', 0)

db.get('ducks')

db.incr('ducks', 2)

db.get('ducks')