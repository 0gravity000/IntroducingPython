# 8-1
test1 = 'This is a test of the emergency text system'
outfile = open('test.txt', 'wt')
outfile.write(test1)
outfile.close

# withを使った場合
with open('test.txt', 'wt') as outfile:
  outfile.write(test1)

# 8-2
test1 = 'This is a test of the emergency text system'
with open('test.txt', 'rt') as infile:
  test2 = infile.read()

test1 == test2

# 8-3
text = '''author, book
J R R Tolkine,The Hobbit
Lynne Truss,"Eate, Shoots & Leaves"
'''
with open('test.csv', 'wt') as outfile:
  outfile.write(text)

# 8-4
import csv

from sqlalchemy.engine import create_engine
with open('test.csv', 'rt') as infile:
  books = csv.DictReader(infile)
  for book in books:
    print(book)

# 8-5
text = '''title,author,year
The Weirstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open('books.csv', 'wt') as outfile:
  outfile.write(text)

# 8-6
import sqlite3
db = sqlite3.connect('books.db')
curs = db.cursor()
curs.execute('''create table book (title text, author text, year int)''')
db.commit()

# 8-7
import csv
import sqlite3
ins_str = 'insert into book values(?, ?, ?)'
with open('books.csv', 'rt') as infile:
  books = csv.DictReader(infile)
  for book in books:
    curs.execute(ins_str, (book['title'], book['author'], book['year']))

db.commit()

# 8-8
# タプル形式で表示
sql = 'select title from book order by title asc'
for row in db.execute(sql):
  print(row)

# タプルを付けずにで表示
sql = 'select title from book order by title asc'
for row in db.execute(sql):
  print(row[0])

sql = '''select title from book order by 
case when (title like "The %") then substr(title, 5) else title end'''
for row in db.execute(sql):
  print(row[0])

# 8-9
for row in db.execute('select * from book order by year'):
  print(row)

for row in db.execute('select * from book order by year'):
  print(*row, sep=', ')

# 8-10
import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = 'select title from book order by title asc'
rows = conn.execute(sql)
for row in rows:
  print(row)

# 8-11
import redis
conn = redis.Redis()
conn.delete('test')
conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})
conn.hgetall('test')

# 8-12
conn.hincrby('test', 'count', 3)
conn.hget('test', 'count')
