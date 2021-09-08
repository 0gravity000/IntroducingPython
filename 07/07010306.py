# 7.1.3.6 パターンの特殊文字
import string
printable = string.printable
len(printable)

printable[0:50]

import re
re.findall('\d', printable)

re.findall('\w', printable)

re.findall('\s', printable)

x = 'abc' + '-/*' + '\u00ea' + '\u0115'

re.findall('\w', x)