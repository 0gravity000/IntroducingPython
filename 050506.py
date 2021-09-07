# 5.5.6 pprint()によるきれいな表示
from pprint import pprint
quotes = OrderdDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Currly', 'Nyuk nyuk!'),
    ])

print(quotes)

pprint(quotes)