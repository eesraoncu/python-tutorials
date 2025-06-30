Question1: Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.
def line(length, string):
    if not string:
        return
    if string[0] == " ":
        print(length * "*")
    else:
        print(length * string[0])
line(7, "%")
line(10, "LOL")
line(3, " ")

Question2: Please write a function named box_of_hashes, which prints out a rectangle of hash characters. The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide. The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in your line function.
def line(length, string):
    if not string:
        return
    if string[0] == " ":
        print(length * "*")
    else:
        print(length * string[0])
def box_of_hashes(height):
    for _ in range(height):
        line(10, "#") 
box_of_hashes(5)

Question3: Please write a function named square_of_hashes, which draws a square of hash characters. The function takes one argument, which determines the length of the side of the square. The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.
def line(length, string):
    if not string:
        return
    if string[0] == " ":
        print(length * "*")
    else:
        print(length * string[0])
def square_of_hashes(length):
    for _ in range(length):
        line(length, "#") 
square_of_hashes(5)
print()
square_of_hashes(3)

Question4: Please write a function named square, which prints out a square of characters, and takes two arguments. The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square. The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.
def line(length, string):
    if not string:
        return
    if string[0] == " ":
        print(length * "*")
    else:
        print(length * string[0])
def square(number, char):
    for _ in range(number):
        line(number, char)
square(5, "*")
print()
square(3, "~")

Question5: Please write a function named triangle, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument. The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.
def line(length, string):
    if not string:
        return
    if string[0] == " ":
        print(length * "*")
    else:
        print(length * string[0])
def triangle(size):
    for i in range(1, size + 1):
        line(i, "#")

Question6: Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it. The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.
def line(length, string):
    if not string:
        return
    if string[0] == " ":
        print(length * "*")
    else:
        print(length * string[0])
def shape(triangle_height, triangle_char, rectangle_height, rectangle_char):
    for i in range(1, triangle_height + 1):
        line(i, triangle_char)
    for _ in range(rectangle_height):
        line(triangle_height, rectangle_char)

Question7: Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.
def spruce(number):
    print(" "*(number-3)+"a spruce!")
    i=number
    row = "*"
    while i > 0:
        print(" " * (i-1) + row)
        row += "**"
        i -= 1
    print(" "*(number-1)+"*")
spruce(5)

Question8: Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three.
def greatest_number(number1,number2,number3):
    print(max(number1, number2, number3))
greatest_number(3, 4, 1)

Question9: Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.
def same_chars(string, index1, index2):
    try:
        return string[index1] == string[index2]
    except IndexError:
        return False
