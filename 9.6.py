def is_abecedarian(word):
	firstLetter = word[0]
	nextLetter = word[1]
	next_letter_i = 1
	for letter in word:
		if ord(letter)>ord(firstLetter);
			return false
	firstLetter = nextLetter
	nextLetter = word[next_letter_i]
	return true
List_of_words = open("words.txt","r")
def calculate_abecedarian():
	count = 0
 	for  word in List_of_words:
		if is_abecedarian(word):
			print(word)
			count+=1
	print(count)
	
calculate_abecedarian()