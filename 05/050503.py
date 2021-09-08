# 5.5.3 OrderedDict()によるキー順のソート
quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk nyuk!',
    }
for stooge in quotes:
    print(stooge)

#
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe': 'A wise guy, huh?'),
    ('Larry': 'Ow!'),
    ('Curly': 'Nyuk nyuk!'),
    ])
for stooge in quotes:
    print(stooge)
