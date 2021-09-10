# 8.2.4 JSON
# JavaScript Object Notation
menu = \
{
    "breakfast": {
        "hours": "7-11",
        "items": {
            "breakfast burritos": "$6.00",
            "pancakes": "$4.00"
            },
        },
    "lunch": {
        "hours": "11-3",
        "items": {
            "humburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
                }
            }
}

# データ構造をJSON文字列にエンコードする
import json
menu_json = json.dumps(menu)
menu_json

# load()で、Pythonデータ構造に戻す
menu2 = json.loads(menu_json)
menu2

import datetime
now = datetime.datetime.utcnow()
now
# エラー JSON標準が日付、時刻型を定義していないため
json.dumps(now)

# datetimeを文字列に変換
now_str = str(now)
json.dumps(now_str)
# datetimeをUnix時間に変換（たぶん）
from time import mktime
now_epoch = int(mktime(now.timetuple()))
json.dumps(now_epoch)

#
class DTEncoder(json.JSONEncoder):
    def defaule(self, obj):
        # instance() は obj の型をチェックする
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        # でなければ普通のデコーダの処理を行う
        return json.JSONEncoder.default(self, obj)

json.dumps(now, cls=DTEncoder)

#
type(now)

isinstance(now, datetime.datetime)

type(234)

isinstance(234, int)

type('hey')

isinstance('hey', str)