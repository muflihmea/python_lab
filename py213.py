string=input("Enter a string")
char_count={}
for char in string:
    char_count[char]=char_count.get(char,0)+1
print("charecter frequncy'",char_count)
