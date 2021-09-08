# 7.1.3.8 パターン：マッチした文字列の出力の指定
source = '''I wish I may, I wish I might Have a dish of fish tonight.'''

import re
m = re.search(r'(. dish\b).*(\bfish', source)
m.group()

# (?P< name > expr )という閉式を使うと exprにマッチした部分はnameという名前のグループに保持される
m = re.search(r'(?P<DISH>). dish\b).*(?P<FISH>\bfish)', source)
m.group()

m.groups()

m.group('DISH')

m.group('FISH')
