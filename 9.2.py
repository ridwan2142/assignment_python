def has_no_e(letter):
    fi = open("words.txt","r")
    c = 0
    no_e = 0
  
    for i in fi:
    word = i.strip()
    if (word.find("e") == -1):
        no_e = no_e + 1
	print(word)
	c = c + 1
    
    percentage = (no_e / c) * 100
    return percentage
