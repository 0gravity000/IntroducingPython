# 4.5 forによる反復処理
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Petar']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

# よりPythonらしいコード
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Petar']
for rabbit in rabbits:
    print(rabbit)

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:     # または for card in accusation.keys():
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

