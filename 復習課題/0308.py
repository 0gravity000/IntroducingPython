# 3-1
years_list = [1973, 1974, 1975, 1976, 1977]
# リスト内包表記を使う場合
years_list = [year for year in range(1973, 1973+5)]
years_list

# 3-2
years_list[3]

# 3-3
years_list[-1]
# or
years_list[5]

# 3-4
things = ["mozzarella", "cinderella", "salmonella"]
things

# 3-5
things[1] = things[1].capitalize()
things
# 以下では書き換わらない
things[1].capitalize()
things

# 3-6
things[0] = things[0].upper()
things

# 3-7
things.remove("salmonella")
things
# or
del things[-1]
# or
del things[2]

# 3-8
surprise = ["Goucho", "Chico", "Harpo"]
surprise

# 3-9
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1].capitalize()
surprise

# 3-10
e2f = { 'dog':'chien', 'cat':'chat', 'walrus':'mouse' }
e2f

# 3-11
e2f['walrus']

# 3-12
f2e = {}
for englihs, france in e2f.items():
  f2e[france] = englihs

f2e

# 3-13
f2e['chien']

# 3-14
set(e2f.keys())

# 3-15
lift = {
  'animals': {
    'cats': [
      'Henri', 'Grumpy', 'Lucy'
    ],
    'octopi': {},
    'emus': {}
  },
  'plants': {},
  'other': {}
}

# 3-16
print(lift.keys())
print(list(lift.keys()))

# 3-17
print(lift['animals'].keys())

# 3-18
print(lift['animals']['cats'])
