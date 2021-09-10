# 8.2.1 CSV
# https://docs.python.org/ja/3/library/csv.html

# 各行に列のリストが含まれているような行のリストを読み書きする方法
import csv
villains = [
    ['Doctor', 'No'],
    ['Rose', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
    ]
with open('./08/villains', 'wt') as fout:    # コンテキストマネージャ
    csvout = csv.writer(fout)
    csvout.writerows(villains)

# リストのリストでファイルを読み出す
import csv
with open('./08/villains', 'rt') as fin: # コンテキストマネージャ
    cin = csv.reader(fin)
    villains = [row for row in cin] # リストの内包表記を使っている
print(villains)

# 辞書のリストでファイルを読み出す
import csv
with open('./08/villains', 'rt') as fin: # コンテキストマネージャ
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin] # リストの内包表記を使っている
print(villains)

# 辞書のリストでファイルを書き込み
import csv
villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rose', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'},
    ]
with open('./08/villains', 'wt') as fout:    # コンテキストマネージャ
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

# データを読み込む
import csv
with open('./08/villains', 'rt') as fin: # コンテキストマネージャ
    cin = csv.DictReader(fin)
    villains = [row for row in cin] # リストの内包表記を使っている
print(villains)
