numbers=input("Enter a list of numbers sperated by space")
numbers = [int (num) for num in numbers.split()]
positive_numbers = [num for num in numbers if num > 0]
squares = [num ** 2 for num in numbers]
word = input("Enter a word")
vowels = [char for char in word if char in 'aeiou']
ordinal_values = [ord(char) for char in word]
print("Postive numbers:", positive_numbers,"Squre Numbers:",squares,"vowels:",vowels,"Ordinal value:",ordinal_values)


