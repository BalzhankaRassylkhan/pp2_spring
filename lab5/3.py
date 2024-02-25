import re

def find_lowercase_sequences(text):
 
  pattern = r"[a-z]+_[a-z]+"
  matches = re.findall(pattern, text)
  return matches

text = "When you_wake up in_the_morning, think about the precious privilege of_being alive_again - to breathe, to_think, to enjoy and to love."

sequences = find_lowercase_sequences(text)

if sequences:
  print("Found sequences:")
  for sequence in sequences:
    print(sequence)
else:
  print("Text is not passed.")
