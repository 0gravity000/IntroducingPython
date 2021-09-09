# 7.1.3.8 パターン：マッチした文字列の出力の指定
source = '''I wish I may, I wish I might Have a dish of fish tonight.'''

# パターンをかっこで囲むとマッチは独自のグループに保存される
# そして、.groups()でそれらのタプルが得られる
import re
m = re.search(r'(. dish\b).*(\bfish)', source)
# group()ですべてのマッチを取り出す
m.group()
# .groups()でそれらのタプルが得られる
m.groups()


# (?P< name > expr )という形式を使うと、
# exprにマッチした部分はnameという名前のグループに保持される
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
m.group()
m.groups()
m.group('DISH')
m.group('FISH')
