""" def checking_sequenceOfNum(list, sequence):
  for i in range(len(list) -len(sequence) + 1):
    if list[i:i+len(sequence)] == sequence:
      return True
  return False



num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sequence = [1, 2, 3, 4, 5]

is_present = checking_sequenceOfNum(num, sequence)
print(is_present) """

def string_mutatuin(input_string):
  strin_shup = []

  for i, char in enumerate(input_string):
    modified_char = char
    if char.isupper():
      modified_char = char.lower() 

    if i % 2 == 0:
        strin_shup.append(modified_char)
    
  return ''.join(strin_shup)

string = 'Hello World'
send_string = string_mutatuin(string)
print(send_string)