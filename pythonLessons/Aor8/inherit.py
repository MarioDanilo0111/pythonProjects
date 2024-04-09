""" class A:
  def __init__(self, value):
    print(f'In A.__init__ = {value}')
    self.value = value

class B(A):
  def __init__(self, value):
    print(f'In B.__init__ = {value}')
    self.value = value

b = B(10)
print(b.value) """


class A:
  def __init__(self, value):
    print(f'In A.__init__ = {value}')
    self.value = value

class B(A):
  def __init__(self, value):
    print(f'In B.__init__ = {value}')
    super().__init__(value)
    self.value += 10

class C(A):
  def __init__(self, value):
    print(f'In C.__init__ = {value}')
    super().__init__(value)
    self.value *= 4


class D(B, C):
  def __init__(self, value):
    print(f'In D.__init__ = {value}')
    super().__init__(value)
   

d = D(10)
print(d.value)
""" Messagen Resulutions order """
print(D.mro())