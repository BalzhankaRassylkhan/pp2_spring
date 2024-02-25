import re

def balzhan(text):
 
  pattern = r"[A-Z][a-z]+"
  matches = re.findall(pattern, text)
  return matches

text = "When You wake up in the morning, Think about the Precious Privilege of being Alive again - to breathe, to think, to enjoy and to love."

sequences = balzhan(text)

if sequences:
  print("Found sequences:")
  for sequence in sequences:
    print(sequence)
else:
  print("Text is not passed.")
