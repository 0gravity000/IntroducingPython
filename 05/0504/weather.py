# 5.4 パッケージ
from sources import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

'''
ファイル構成
weather.py
└─sources/
    │─  __init__.py #このファイルがあるディレクトリをパッケージとして扱う。中身はからでもよい
    │─  daily.py
    └─  weekly.py


実行
python weather.py

Daily forecast: like yesterday
Weekly forecast:
1 snow
2 more snoe
3 sleet
4 freezing rain
5 rain
6 fog
7 hair

'''