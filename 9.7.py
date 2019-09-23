file = open('words.txt','r')
def three_consequtive_double(word):
    
    count_position = 0
    index_position = 0
    while index_position < len(word)-1:
      if word[index_position] == word[index_position+1]:
        count_position = count_position + 1
        if count_position == 3:
          return True
        index_position = index_position + 2
      else:
        count_position = 0
        index_position = index_position + 1
total_count = 0
for line in file:
  word = line.strip()
  if three_consequtive_double(word) != False:
    print("The word is: ", word)
    total_count = total_count + 1

print("The count is: ", total_count)