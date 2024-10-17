numbers=[int(x) for x in input("enter a list of integers (space.seprated)").split()]
odd_number=[num for num in numbers if num % 2 != 0]
print("List after remove memmory even numbers",odd_number)
