words=input("Enter a list of word(space-speeated):").split()
longest_word=max(words,key=len)
print("Longest word is :",longest_word,"with length",len(longest_word))
