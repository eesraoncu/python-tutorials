Question1: Please write a program which asks the user for an integer number. The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.
while True:
  number=int(input("Please type in a number: "))
  if number == 1984:
    print("Orwell")
  else:
     break

Question2: Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is. 
while True:
  number=int(input("Please type in a number: "))
  if number<0:
    print(-1*number)
  else:
    print(number)
  break

Question3: Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.
while True:
  name=input("Please tell me your name: ")
  if name=="Jerry":
    print("Next please!")
    break
  else:
    portion=int(input("How many portions of soup?"))
    print("The total cost is",portion*5.90)
    print("Next please!")

Question4: Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number.
number = int(input("Please type in a number: "))
if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")
print("Thank you!")

Question5: Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.
number1=int(input("Please type in a number:"))
number2=int(input("Please type in second number:"))
operation_name=input("Please type in an operation:")
if operation_name=="add":
  print(number1,"+",number2,"=",number1+number2)
elif operation_name=="multiply":
  print(number1,"*",number2,"=",number1*number2)
elif operation_name=="subtract":
  print(number1,"-",number2,"=",number1-number2)

Question6: Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".
temperature=int(input("Please type in a temperature (F): "))
celcius=(temperature-32)*(5/9)
if celcius<0:
  print(temperature,"degrees Fahrenheit equals",celcius,"degrees Celsius")
  print("Brr! It's cold in here!")
else:
  print(temperature,"degrees Fahrenheit equals",celcius,"degrees Celsius")

Question7: Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.
hourly_wage=float(input("Hourly wage::"))
daily_work_hour=int(input("Hours worked:"))
day=input("Day of the week:")
if day.upper() =="SUNDAY":
    hourly_wage=hourly_wage*2
print("Daily wages:",hourly_wage*daily_work_hour)

Question8: This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated with the following formula:
If there are less than a hundred points on the card, the bonus is 10 %
In any other case the bonus is 15 %
But there is a problem with the program, so with some inputs it doesn't work quite right. Please fix the program so that there is always either a 10 % or a 15 % bonus, but never both.
*Wrong State*                                                     *Correct State*
points = int(input("How many points are on your card? "))         points = int(input("How many points are on your card? "))
if points < 100:                                                  if points < 100:
    points *= 1.1                                                      print("Your bonus is 10 %")
    print("Your bonus is 10 %")                                        points *= 1.10
if points >= 100:                                                 else:
    points *= 1.15                                                      print("Your bonus is 15 %")
    print("Your bonus is 15 %")                                          points *= 1.15
print("You now have", points, "points")                           print("You now have", points, "points")

Question9: Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing. The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.
print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")
if temperature <= 20:
    print("I recommend a jumper as well")
if temperature <= 10:
    print("Take a jacket with you")
if temperature <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain.lower() == "yes":
    print("Don't forget your umbrella!")

Question10: Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation.
from math import sqrt
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))
discriminant = b**2 - 4*a*c
if discriminant < 0:
    print("Error: The equation has no real roots.")
else:
    root1 = (-b + sqrt(discriminant)) / (2*a)
    root2 = (-b - sqrt(discriminant)) / (2*a)
    print("\nThe roots are",root1,"and",root2)                                         
