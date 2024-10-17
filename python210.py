color_list1=input("ENter color for list1 for seprated by space").split()
color_list2=input("ENter color for list2 for seprated by space").split()
unique_color=[color for color in color_list1 if color not in color_list2]
print("Color in list1 But not on this list 2",unique_color)

