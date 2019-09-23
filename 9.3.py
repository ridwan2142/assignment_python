book = open('words.txt','r')
def avoids(word1,String_of_forbidden_letters):
    for word2 in String_of_forbidden_letters:
        if word2 in word1:
            return False
    return True


def avoid_w():
  c1 = 0
  string1 = input("Write the forbidden letters?")
  string1 = string1.lower()
  

  for line in book:
      word = line.strip()
    if avoids(word1,string1):
          c1 = c1 +1
  return c1