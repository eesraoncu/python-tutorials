Question1: Let's create a program along the lines of the example above. This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish. 
while True:
    print("hi")
    answer = input("Shall we continue? ")
    if answer == "no":
        break
print("okay then")

Question2: Write a program that asks for numbers repeatedly. If the number is positive, print its square root. If it's negative, print "Invalid number". If it's 0, print "Exiting..." and stop.
from math import sqrt
while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        print("Exiting...")
        break
    elif number < 0:
        print("Invalid number")
    else:
        print(sqrt(number))

Question3: This program should print out a countdown.
*Wrong State*                              *Correct State*
number = 5                                 number = 5
print("Countdown!")                        print("Countdown!")
while True:                                while number > 0:
  print(number)                                 print(number)
  number = number - 1                           number = number - 1
  if number > 0:                           print("Now!")
    break
print("Now!")

Question4: Please write a program which asks the user for a password. The program should then ask the user to type in the password again. If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.
password = input("Password: ")
repeat = input("Repeat password: ")
while repeat != password:
    print("They do not match!")
    repeat = input("Repeat password: ")
print("User account created!")

Question5: Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.
attempts = 1
pin = input("PIN: ")
while pin != "4321":
    print("Wrong")
    attempts += 1
    pin = input("PIN: ")
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print("Correct! It took you",attempts,"attempts")

Question6:Please write a program which asks the user for a year, and prints out the next leap year.
year = int(input("Year: "))
year += 1
while True:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("The next leap year after",year - 1,"is",year)
        break
    year += 1

Question7: Part1:Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.
story = ""
while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    if story == "":
        story = word
    else:
        story += " " + word
print(story)

Part2: Change the program so that the loop ends also if the user types in the same word twice in a row.
story = ""
previous = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == previous:
        break
    if story == "":
        story = word
    else:
        story += " " + word
    previous = word
print(story)

Question8: Pre-task: Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number: "))
    if number == 0:
        break

Part 1: Count: After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    count += 1
print("Numbers typed in", count)

Part2: Sum: The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
total = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    count += 1
    total += number
print("Numbers typed in", count)
print("The sum of the numbers is", total)

Part 3: Mean: The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
total = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    count += 1
    total += number
mean = total / count
print("Numbers typed in", count)
print("The sum of the numbers is", total)
print("The mean of the numbers is", mean)

Part 4: Positives and negatives: The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
total = 0
positives = 0
negatives = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    count += 1
    total += number
    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1
mean = total / count
print("Numbers typed in", count)
print("The sum of the numbers is", total)
print("The mean of the numbers is", mean)
print("Positive numbers", positives)
print("Negative numbers", negatives)
