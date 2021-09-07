# 8.2.1 CSV
import csv
villains = [
    ['Doctor', 'No'],
    ['Rose', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
    ]
with open('villains', 'wt') as fout:    # コンテキストマネージャ
    csvout = csv.writer(fout)
    csvout.writerows(villains)

import csv
with open('villains', 'rt') as fin: # コンテキストマネージャ
    cin = csv.reader(fin)
    villains = [row for row in cin] # リストの内包表記を使っている
print(villains)

import csv
with open('villains', 'rt') as fin: # コンテキストマネージャ
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin] # リストの内包表記を使っている
print(villains)

import csv
villains = [
    ('first': 'Doctor', 'last': 'No'),
    ('first': 'Rose', 'last': 'Klebb'),
    ('first': 'Mister', 'last': 'Big'),
    ('first': 'Auric', 'last': 'Goldfinger'),
    ('first': 'Ernst', 'last': 'Blofeld'),
    ]
with open('villains', 'wt') as fout:    # コンテキストマネージャ
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

import csv
with open('villains', 'rt') as fin: # コンテキストマネージャ
    cin = csv.DictReader(fin)
    villains = [row for row in cin] # リストの内包表記を使っている
print(villains)