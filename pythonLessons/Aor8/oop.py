class person:
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
  def myfunc(self):
    return f'{self.name} is {self.age} years old and has email {self.email}'
    

p1 = person("John",'john@email', 36)
p2 = person("Jane",'jane@email', 34)

print(p1)
print(p2)

p1.phone = '0712345678'

print(p1.phone)
print(p2.phone)
