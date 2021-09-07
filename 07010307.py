# 7.1.3.7 パターン：メタ文字
source = '''I wish I may, I wish I might Have a dish of fish tonight.'''

import re

re.findall('wish', source)

re.findall('wish|fish', source)

re.findall('^wish', source)

re.findall('^I wish', source)

re.findall('fish$', source)

re.findall('fish tonight.$', source)

# ^ と $ はアンカー（錨）と呼ばれる
# ^ はサーチをソース文字列の先頭に固定
# $ はサーチをソースの末尾に固定する
# .$は、行末の任意の文字（ピリオドを含む）にマッチする
# より正確にリテラルにマッチさせるには、ドットをエスケープする（ドットの前にエスケープ文字の\を置く）
re.findall('fish tonight\.$', source)

re.findall('[wf]ish', source)

re.findall('[wsh]+', source)

re.findall('ght\W', source)

re.findall('I (?=wish)', source)

re.findall('(?<=I) wish', source)

# 期待通りに動かない
re.findall('\bfish', source)
# 以下は期待どおりに動く
re.findall(r'\bfish', source)
