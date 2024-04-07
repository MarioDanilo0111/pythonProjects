""" def func(*args):
  print(args)

func()
func(1)
func(1, 2)
func(1, 2, 3)
 """

""" def func(a,b, **kwargs):
  print(a,b)
  print(kwargs)

func(1, 2, c=3, d=4) """

""" def func(a,b, **kwargs):
  print(a,b, kwargs['c'], kwargs['d'])  

func(1, 2, c=3, d=4) """

""" def func(a,b, **kwargs):
  print(a,b)  
  if 'c' in kwargs:
    print(kwargs['c'])
  if 'd' in kwargs:
    print(kwargs['d'])

func(1, 2, d=7) """

def fuc(a,b, *args, names='john', **kwargs):
  print(f'a = {a}')
  print(f'b = {b}')
  print(f'args = {args}')
  print(f'names = {names}')
  print(f'kwargs = {kwargs}') #dictonary
fuc(1, 2, 3, name='bob', age=20, email='VhT6p@example.com')