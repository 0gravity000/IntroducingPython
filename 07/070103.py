# 7.1.3 正規表現とのマッチング
import re
# Youはパターン、Young Frankensteinはソース
result = re.match('You', 'Young Frankenstein')

youpattern = re.compile('You')

result = youpattern.match('Young Frankenstein')