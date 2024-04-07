""" value = [1,2,3,4,]
#List Comprehension

new_value = [value**2 for value in value]
print(type(new_value))

#set Comprehension
new_set = {value**2 for value in value}
print(type(new_set))

#Dictionary Comprehension
new_dict = {value: value**2 for value in value}
print(type(new_dict))
print(new_dict)  """

#Tuple Comprehension
value = [1,2,3,4,5]
new_tuple = (value**2 for value in value)
print(type(new_tuple))
value = [1,2,3,4,5]
#create a list
new_tuple = ([value**2 for value in value])
print(type(new_tuple))