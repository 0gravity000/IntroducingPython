# 5.3.3 必要なものだけをインポートする方法
from report import get_description
descrioption = get_description()
print("Today's weather:", descrioption)

#
from report import get_description as do_it
descrioption = do_it()
print("Today's weather:", descrioption)
