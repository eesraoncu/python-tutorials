Question1: Please write a program which asks for the user's age. If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.
age = int(input("What is your age? "))
if age < 0:
    print("That must be a mistake.")
elif age < 5:
    print("I suspect you can't write quite yet...")
else:
    print("Ok, you're",age,"years old.")

Question2: Please write a program which asks for the user's name. If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews. In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.
name = input("Please type in your name: ")
if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

Question3: Please write a program which asks for the number of points received (between 0 and 100). Based on the input, the program should print out the corresponding grade.
points = int(input("How many points [0-100]: "))
if points < 0 or points > 100:
    print("Grade: impossible!")
elif points < 50:
    print("Grade: fail")
elif points < 60:
    print("Grade: 1")
elif points < 70:
    print("Grade: 2")
elif points < 80:
    print("Grade: 3")
elif points < 90:
    print("Grade: 4")
else:
    print("Grade: 5")

Question4: Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.
number = int(input("Number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")

Question5: Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.
year = int(input("Please type in a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

Question6: Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
a = input("1st letter: ")
b = input("2nd letter: ")
c = input("3rd letter: ")
if (a <= b <= c) or (c <= b <= a):
    middle = b
elif (b <= a <= c) or (c <= a <= b):
    middle = a
else:
    middle = c
print("The letter in the middle is", middle)

Question7:Please write a program which calculates the correct amount of tax for a gift from a close relative.
value_of_gift=int(input("Value of gift:"))
if value_of_gift<5000:
    print("No tax!")
else:
   if value_of_gift>=5000 and value_of_gift<=25000:
    tax=100+(value_of_gift-5000)*0.08
   elif value_of_gift>25000 and value_of_gift<=55000:
    tax=1700+(value_of_gift-25000)*0.1
   elif value_of_gift>55000 and value_of_gift<=200000:
    tax=4700+(value_of_gift-55000)*1.2
   elif value_of_gift>200000 and value_of_gift<=1000000:
    tax=22100+(value_of_gift-200000)*1.5
   elif value_of_gift>1000000:
    tax=142100+(value_of_gift-1000000)*1.7
print("Amount of tax:",tax)
