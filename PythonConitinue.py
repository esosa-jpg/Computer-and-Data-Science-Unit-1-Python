userWord = input("enter a word ")
for letter in userWord:
  if letter.upper() == "A" or letter.upper() == "E" or letter.upper() == "I" or letter.upper() == "O" or letter.upper() == "U":
      continue
  print(letter)
