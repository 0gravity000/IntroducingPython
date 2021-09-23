# 5.3.2 別名によるモジュールのインポート
import report as wr #reportモジュール全体をwrという別名でインポート
descrioption = wr.get_description()
print("Today's weather:", descrioption)