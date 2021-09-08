# 8.2.4 JSON
menu = ¥
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

import json
menu_json = json.dumps(mene)
menu_json

menu2 = json.loads(menu_json)
menu2

import datetime
now = datetime.datetime.utcnow()
now

json.dumps(now)

#
now_str = str(now)
json.dumps(now_str)

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