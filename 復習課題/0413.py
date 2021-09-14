# 4-1
guess_me = 7
if ( guess_me < 7 ):
  print('too low')
elif( guess_me > 7 ):
  print('too high')
else:
  print('just right')

# 4-2
guess_me = 7
start = 1
while True:
  if ( start < guess_me ):
    print('too low')
  elif( start == guess_me ):
    print('found it!')
    break
  elif( start > guess_me ):
    print('oops')
  start += 1

# 4-3
for val in [3, 2, 1, 0]:
  print(val)

# 4-4
even = [number for number in range(10) if number % 2 == 0]
even

# 4-5
squares = {key: key*key for key in range(10)}
squares

# 4-6
odd = {number for number in range(10) if number % 2 == 1}
odd

# 4-7
for thing in ('Got %s' % number for number in range(10)):
  print(thing)

# 4-8
def good():
  return ['Harry', 'Ron', 'Harmione']

good()

# 4-9
def get_odds():
  for number in range(1, 10, 2):
    yield number

for count, number in enumerate(get_odds(), 1):
  if count == 3:
    print("The third odd number is", number)
    break

# 4-10
def test(func):
  def new_func(*args, **kwargs):
    print('statr')
    result = func(*args, **kwargs)
    print('end')
    return result
  return new_func

@test
def greeting():
  print("Greetings, Earthling")

greeting()

# 4-11
class OopsException(Exception):
  pass

raise OopsException()

try:
  raise OopsException
except OopsException:
  print('Caught an oops')

# 4-12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
movies

