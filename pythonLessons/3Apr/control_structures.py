#for loop

""" for i in range(5):
  print(i) """

""" for i in range(2,5):
  print(i) """

""" for i in range(1,10,2):
  print(i) """

""" for i in  range(10):
  in i == 5:
    continue
    print(i) """

""" for i in range(10):
  if i == 5:
    break
  print(i)
  if i == 7:
    break

print("done") """


""" for i in range(10):
  if i == 5:
    continue
  print(i)
  if i == 7:
    break
else:
  print("else")

print("done")
 """

""" for i in range(10):
  if i == 5:
    continue
  print(i)
  if i == 7:
    found = True
    break
else:
  print("else")

print("done") """
  
""" for i in [1, 2, 3, 'Anna', True]:
  print(i) """

""" for i in [1, 2, 3, 'Anna', True]:
  print('Hej',i) """

""" for i, value in enumerate(['Fnatte', 'Knatte','Tjatte', 'Kalle'], 10):
  print(i, value) """

""" values = list(range(1000))
print(values) """

""" values = set(range(2, 100, 4))
print(values) """

#if statemetent:
""" 
x = 10
y = 10

if x > 10:
  print("x is bigger than 10")
else:
  print("x is not bigger than 10, could be equal or less than 10")
   """

""" x = 10
y = 10

if x > 10 and y == 20:
  print("x is bigger than 10 and y is 10")
else:
  print("x is not bigger than 10, could be equal or less than 10") """
""" x = 10
y = 10

if x > 10 or y == 20:
  print("x is bigger than 10 and y is 10")
else:
  print("x is not bigger than 10, could be equal or less than 10") """
 
""" grade = 25

if grade < 10:
  print("Poor")
else:
  if grade < 20:
    print("Average")
  else:
    if grade < 30:
      print("Good")
    else:
      print("Excellent") """
""" 

#ELIF
grade = 25

if grade < 10:
  print("Poor")
elif grade < 20:
    print("Average")
elif grade < 30:
  print("Good")
else:
  print("Excellent")
 """

#while loop

x = 10
while x < 44:
  print(x)
  x *= 2