def uses_all(word1, char):
    required_letters = char.strip()
    for letter in required_letters:
        if letter not in word:
            return False
    return True
book = open('words.txt',"r")
index = 0
for line in book:
    word = line.strip()
    vowels  = 'aeiou'
    if uses_all(word,vowels):
        print(word)
        index += 1
print(index)