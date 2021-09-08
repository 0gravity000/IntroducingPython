# 5.5.1 setdefault()とdefaultdict()による存在しないキーの処理
periodic_table = ['Hydrogen': 1, 'Helium':2]
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
carbon

periodic_table

helium = periodic_table.setdefault('Helium', 947)
helium

periodic_table

#
from collection import defaultdict
periodic_table = defaultdict(int)

periodic_table['Hydrogen'] = 1
periodic_table['Lead']

periodic_table

#
from collections import defaultdict

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'

bestiary['A']
bestiary['B']
bestiary['C']

#
bestiary = defaultdict(lambda: 'Huh?')
bestiary['E']

from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

#
dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] == 1

for food, count in dict_counter.items():
    print(food, count)