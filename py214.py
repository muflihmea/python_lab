string=input("Enter a string:")
if string.endswith("ing"):
    modified_string=string+'ly'
else:
    modified_string=string+'ing'
print("Modified string:",modified_string)
