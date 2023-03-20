def count_numbers(text):
  dictionary = {} 
  for number in text:
    if number == int:
     if number in dictionary:
          dictionary.update({text, number})
     number += number
  return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}
