# 8.5.2 memcached
import memcache
db = memcache.Client(['127.0.0.1:11211'])
db.set('macro', 'polo')

db.get('macro')

db.set('ducks', 0)

db.get('ducks')

db.incr('ducks', 2)

db.get('ducks')