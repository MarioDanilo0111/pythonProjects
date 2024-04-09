""" def checking_sequenceOfNum(list, sequence):
  for i in range(len(list) -len(sequence) + 1):
    if list[i:i+len(sequence)] == sequence:
      return True
  return False



num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sequence = [1, 2, 3, 4, 5]

is_present = checking_sequenceOfNum(num, sequence)
print(is_present) """

""" def string_mutatuin(input_string):
  strin_shup = []

  for i, char in enumerate(input_string):
    if char.isupper():
      char.lower() 
    if i % 2 == 0:
        strin_shup.append(char)
    
  return ''.join(strin_shup)

string = 'Hello World'
send_string = string_mutatuin(string)
print(send_string) """

""" def multiple_str_back(string_input):

  char_times_two = []

  for char in string_input:
   char_times_two.append(char*2)

  return ''.join(char_times_two) 

string = 'Hello World'
duble_string = multiple_str_back(string)
print(duble_string)
 """

""" def count_of_even_nums(list_of_nums):
  count = 0
  for sublist in list_of_nums:
      for num in sublist:
        if num % 2 == 0:
          count += 1
  return count

list_of_nums = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19], [12, 14, 16, 18, 20]]
return_value = count_of_even_nums(list_of_nums)
print(return_value) """

""" import random 

def guess_number():
  digits = [str(random.randint(1, 9))]
  while len(digits) < 3:
    new_digit = str(random.randint(0, 9))
    if new_digit not in digits:
      digits.append(new_digit)
  random_nr_str = ''.join(digits)
  
  random_number_str = str(random_nr_str)
  user_guess_str = str(user_guess)

  random_digit_set = set(random_number_str)
  user_digit_set = set(user_guess_str)

  #  print('Guess a 3-digit number: ')  

  while True:
     user_guess = input(
       'Enter your guess: '
     )
     

     if len(user_guess) != 3:
         print('The digit lenghts are not the same, try again:')
         continue
     
     common_digits = random_digit_set.intersection(user_digit_set)
  
      # correct_digit = [digit for digit, guess in zip(random_nr_str, user_guess) if digit == guess] 
    
     if len(common_digits) == 3:
       print('You guessed the correct number!')
       break
     if common_digits:
       print(f"This digits are correct: {' '.join(common_digits)}")
     else:
        print('No digits are correct, try again!')
    
  print(f'The correct number is: {random_nr_str}')

guess_number()
 """