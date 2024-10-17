color_input=input("Enter comma seprated color names:")
color_list=color_input.split(",")
color_list=[color.strip() for color in color_list]
if color_list:
    print("first color:",color_list[0])
    print("Last color:",color_list[-1])
else:
    print("no color were eneterd")

