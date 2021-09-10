# 8.5 NoSQLデータストア
# no SQL、not only SQL

# 8.5.1 dbmファミリ
# dbmはキーバリューストア（複数のキーと値のペア）で、
# ウェブブラウザなどのアプリでさまざまな設定を維持・管理するために組み込まれていることが多い
# Pythonの辞書と似ている

import dbm
db = dbm.open('difinitions', 'c')

db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'

len(db)

db['pesto']

db.close()
db = dbm.open('difinitions', 'r')
db['mustard']