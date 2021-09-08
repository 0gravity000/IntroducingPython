# 8.5.1 dbmファミリ
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