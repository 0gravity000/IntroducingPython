# 10.4 カレンダーとクロック

# 10.4.1 datetimeモジュール
# 標準ライブラリのdatetimeモジュールには4つのメインオブジェクトがある
# dateオブジェクト  年月日対象
# timeオブジェクト  時分秒を対象
# datetimeオブジェクト  日付と時刻の両方を対象
# timedeltaオブジェクト 時付と時刻の間隔を対象
from datetime import date
halloween = date(2014, 10, 31)
halloween
halloween.day
halloween.month
halloween.year
halloween.isoformat()

from datetime import date
now = date.today()
now

from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
tomorrow
# 17日後
now + 17*one_day

yestaday = now - one_day
yestaday

from datetime import time
noon = time(12, 0, 0)
noon
noon.hour
noon.minute
noon.second
noon.microsecond

from datetime import datetime
some_day = datetime(2014, 1, 2, 3, 4, 5, 6)
some_day

some_day.isoformat()

from datetime import datetime
now = datetime.now()
now
now.year
now.month
now.day
now.hour
now.minute
now.second
now.microsecond

from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
noon_today

noon_today.date()
noon_today.time()

# 10.4.2 timeモジュールの使い方
# datetimeモジュールのtimeオブジェクトでなくtimeモジュールもある
# Unix時間  1970年1月1日午前0時からの秒数 エポックとも呼ばれる
# これはシステムの間で日時を交換するための方法としてもっとも簡単

# timeモジュールのtime()は、Unix時間で表現した現在の時刻を返す
import time
now = time.time()
now
# ctime()は、Unix時間を文字列に変換できる
time.ctime(now)
# localtime()はシステムの標準時での日時を返す
time.localtime(now)
# UTC 協定世界時 Coordinated Universal Time 旧グリニッジ標準時間 の時間で返す
time.gmtime(now)
# Unix時間に変換する
tm = time.localtime(now)
time.mktime(tm)

# サーバーには時刻にUTCを使うこと。各地の標準時にしない。
# 時刻はUTC、文字列はUTF-8を使う

# 10.4.3 日時の読み書き
now = time.time()
time.ctime(now)

# strfime()で日時データを文字列に変換できる
fmt = "It's %A, %B, %d, %Y, loact time %I:%M:%S%p"
t = time.localtime()
t
time.strftime(fmt, t)

from datetime import date
some_day = date(2014, 7, 4)
some_day.strftime(fmt)

from datetime import time
some_day = time(10, 35)
some_day.strftime(fmt)

import time
fmt = "%Y-%m-%d"
time.strptime("2012-01-29",fmt)

# ロケールによって名前は変わる
# setlocale()でロケールを変更する
import locale
from datetime import date
halloween = date(2014, 10, 31)
for lang_country in ['rn_us', 'fr_fr', 'da_de', 'es_es', 'is_is', 'ja_JP']:
  locale.setlocale(locale.LC_TIME, lang_country)
  halloween.strftime('%A, %B, %d')

# ロケールの一覧
import locale
names = locale.locale_alias.keys()
names

good_names = [name for name in names if len(name) == 5 and name[2] == '_']
good_names

good_names[:5]

de = [name for name in good_names if name.startswith('de')]
de

# 10.4.4 代替モジュール
# arrow
# dateutil
# iso8601
# fleming
