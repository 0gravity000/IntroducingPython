empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

another_empty_list = list()
another_empty_list

list('cat')

a_tuple = ('ready', 'fire', 'aim')
list(a_tuple)

birthday = '1/6/1952'
birthday.split('/')

splitme = 'a/b//c/d///e'
splitme.split('/')

splitme.split('//')

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0]

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0:2]

marxes.append('Zeppo')
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(3, 'Gummo')
marxes

marxes.insert(10, 'Karl')
marxes

del marxes[-1]
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes[2]
del marxes[2]
marxes
marxes[2]

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.remove('Gummo')
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.pop()
marxes
marxes.pop(1)
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.index('Chico')

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
'Groucho' in marxes
'Bob' in marxes

words = ['a', 'deer', 'a', 'female', 'deer']
'deer' in words

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.count('Harpo')

marxes.count('Bob')

snl_skit = ['cheesebuger', 'cheesebuger', 'cheesebuger']
snl_skit.count('cheesebuger')

marxes = ['Groucho', 'Chico', 'Harpo']
', ' .join(marxes)  #join()はspｨt()の逆

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
joined
separated = joined.split(separator)
separated
separated == friends

marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
sorted_marxes
marxes
marxes.sort()
marxes

numbers = [2, 1, 4.0, 3]
numbers.sort()
numbers

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
numbers

marxes = ['Groucho', 'Chico', 'Harpo']
len(marxes)

a = [1, 2, 3]
a
b = a
b
a[0] = 'surprise'
a
b   #ここ重要
b[0] = 'I hate surprises'
b
a

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 'integer lists are boring'
a
b
c
d

empty_tuple = ()
empty_tuple

one_marx = 'Groucho',
one_marx

marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_tuple

marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_tuple

marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple    #タプルのアンパック
a
b
c

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
password
icecream

marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)

#辞書 連想配列 ハッシュ ハッシュマップ dict
empty_dict = {}
empty_dict

lol = [['a', 'b'], ['c', 'b'], ['e', 'f']]
dict(lol)

lot = [('a', 'b'), ('c', 'b'), ('e', 'f')]
dict(lot)

tol = (['a', 'b'], ['c', 'b'], ['e', 'f'])
dict(tol)

los = ['ab', 'cd', 'ef']
dict(los)

tos = ('ab', 'cd', 'ef')
dict(tos)

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Falin': 'Michael',
}
pythons

pythons['Gilliam'] = 'Garry'
pythons

pythons['Gilliam'] = 'Terry'
pythons

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Falin',
    'Terry': 'Jones',
}
some_pythons

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Falin': 'Michael',
}
pythons
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
pythons

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
first

del pythons['Marx']
pythons
del pythons['Howard']
pythons

pythons.clear()
pythons
pythons = {}
pythons

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Jones': 'Terry',
    'Falin': 'Michael',
}
pythons
'Chapman' in pythons
'Falin' in pythons
'Gilliam' in pythons

pythons['Cleese']
pythons['Marx']
'Marx' in pythons
pythons.get('Marx', 'Not a Python')
pythons.get('Marx')

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
signals.keys()

list(signals.values())

list(signals.items())

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
save_signals

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
signals
original_signals

empty_set = set()
empty_set
even_numbers = {0, 2, 4, 6, 8}
even_numbers
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers

set('letters')

set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])

set(('Ummagumma', 'Echoes', 'Atom Heart Mother'))

set({'apple': 'red', 'orage': 'orange', 'cherry': 'red'})

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_list[2]
marx_tuple[2]
marx_dict['Harpo']

marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes, pythons, stooges
tuple_of_lists

list_of_lists = [marxes, pythons, stooges]
list_of_lists

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges':stooges}
dict_of_lists

houses = {
    (44.79, -93.14, 285): 'My House',
    (38.89, -77.03, 13): 'The White House',
}
