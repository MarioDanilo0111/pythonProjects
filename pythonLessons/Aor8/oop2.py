""" Kwargs """

class person:
  def __init__(self, **kwargs):
    self.__dict__ = (kwargs)

  def __str__(self):
    return f'{self.name} is {self.age} years old.'

p1 = person(name="John", email="john@email", age=36)
p2 = person(name="Jane", email="jane@email", age=34)
print(p1)
print(p2)