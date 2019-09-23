def uses_only(word,String_of_letters):
  for letter in word:
      if letter not in String_of_letters:
        return False
  return True