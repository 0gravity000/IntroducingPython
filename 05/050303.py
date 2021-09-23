# 5.3.3 必要なものだけをインポートする方法
# Pythonでは、モジュールからひとつ以上の部品だけをインポートすることができる
from report import get_description  #reportモジュールからget_description()関数をインポート
descrioption = get_description()
print("Today's weather:", descrioption)

#
from report import get_description as do_it #reportモジュールからget_description()関数をdo_itという別名でインポート
descrioption = do_it()
print("Today's weather:", descrioption)
