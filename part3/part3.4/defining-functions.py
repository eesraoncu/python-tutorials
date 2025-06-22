Question1: Please write a function named seven_brothers. When the function is called, it should print out the names of the seven brothers in alphabetical order.
def seven_brothers():
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")
seven_brothers()

Question2: The exercise contains the outline of the function first_character. Please complete it so that it prints out the first character of the string it takes as its argument.
def first_character:
    print(word[0])
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

Question3: Please write a function named mean, which takes three integer arguments. The function should print out the arithmetic mean of the three arguments.
def mean(number1,number2,number3):
    mean=(number1+number2+number3)/3
    print(mean)
mean(5,3,1)

Question4: Please write a function named print_many_times(text, times), which takes a string and an integer as arguments. The integer argument specifies how many times the string argument should be printed out.
def print_many_times(text, times):
    for _ in range(times):
        print(text)
print_many_times("hi", 5)

Question5: Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square.
def hash_square(length):
  for i in range(length):
    print('#' * length)
hash_square(5)

Question6: Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board.
def chessboard(size):
    for row in range(size):
        line = ""
        for col in range(size):
            if (row + col) % 2 == 0:
                line += "1"
            else:
                line += "0"
        print(line)
chessboard(3)

Question7: Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters.
def squared(text, size):
    for i in range(size):
        line = ""
        for j in range(size):
            index = (i + j) % len(text)
            line += text[index]
        print(line)
squared("esra", 3)
