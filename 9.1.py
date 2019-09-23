def program():
  fi = open("words.txt","r")

  for li in fi:
    
    if len(words) > 20:
	words = li.strip()
      	print(words)