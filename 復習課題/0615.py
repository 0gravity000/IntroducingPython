# 6-1
class Thing:
  pass

example = Thing()

print(Thing)
print(example)

# 6-2
class Thing2:
  letters = 'abc'

print(Thing2.letters)

# 6-3
class Thing3:
  def __init__(self):
    self.letters = 'xyz'

print(Thing3.letters) # lettersはクラス属性ではないのでエラー

something = Thing3()
print(something.letters)

# 6-4
class Element:
  def __init__(self, name, symbol, number):
      self.name = name
      self.symbol = symbol
      self.number = number

hydrogen = Element('Hydrogen', 'H', '1')

# 6-5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
hydrogen.name

# or
hydrogen = Element(**el_dict)
hydrogen.name

# 6-6
class Element:
  def __init__(self, name, symbol, number):
      self.name = name
      self.symbol = symbol
      self.number = number
  def dump(self):
    print('name=%s, symbole=%s , number=%s' % 
    (self.name, self.symbol, self.number))

hydrogen = Element(**el_dict)
hydrogen.dump()

# 6-7
print(hydrogen)

class Element:
  def __init__(self, name, symbol, number):
      self.name = name
      self.symbol = symbol
      self.number = number
  def __str__(self):
    print('name=%s, symbole=%s , number=%s' % (self.name, self.symbol, self.number))

hydrogen = Element(**el_dict)
print(hydrogen)

# 6-8
class Element:
  def __init__(self, name, symbol, number):
      self.__name = name
      self.__symbol = symbol
      self.__number = number
  @property
  def name(self):
    return self.__name
  @property
  def symbol(self):
    return self.symbol
  @property
  def number(self):
    return self.number

hydrogen = Element('Hydrogen', 'H', '1')
hydrogen.name
hydrogen.symbol
hydrogen.number

# 6-9
class Bear:
  def eats(self):
    return 'berries'

class Rabbit:
  def eats(self):
    return 'clover'

class Octothorpe:
  def eats(self):
    return 'campers'

b = Bear()
r = Rabbit()
o = Octothorpe()
print(b.eats())
print(r.eats())
print(o.eats())

# 6-10
class Leser:
  def does(self):
    return 'disintegrate'

class Claw:
  def does(self):
    return 'crush'

class SmartPhone:
  def does(self):
    return 'ring'

class Robot:
  def __init__(self):
    self.laser = Leser()
    self.claw = Claw()
    self.smartphone = SmartPhone()
  def does(self):
    return '''
    I have many attachments: My laser, to %s. My claw, to %s. My smartphone, to %s
    ''' % (self.laser.does(), self.claw.does(), self.smartphone.does())

robbie = Robot()
print(robbie.does())
