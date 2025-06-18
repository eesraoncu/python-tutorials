Question1: Please write a program which asks the user for a number. The program then prints out the number multiplied by five.
number=int(input("Please enter a number: "))
print(number,"times","5 is",number*5)

Question2: Please write a program which asks the user for their name and year of birth.
name=input("What is your name?")
year=int(input("Which year were you born?"))
print("Hi",name,"you will be",2025-year,"years old at the end of the year 2025.")

Question3: Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.
number_of_days=int(input("How many days:"))
print("Seconds in that many days:",number_of_days*3600*24)

Question4: This program asks the user for three numbers. The program then prints out their product, that is, the numbers multiplied by each other. There is, however, something wrong with the program - it doesn't work quite right, as you can see if you run it. Please fix it.
*Wrong State*                                                     *Correct State*
number = int(input("Please type in the first number: "))          number1 = int(input("Please type in the first number: "))
number = int(input("Please type in the second number: "))         number2 = int(input("Please type in the second number: "))
number = int(input("Please type in the third number: "))          number3 = int(input("Please type in the third number: "))
product = number * number * number                                product = number1 * number2 * number3
print("The product is", product)                                  print("The product is", product)

Question5: Please write a program which asks the user for two numbers. The program will then print out the sum and the product of the two numbers.
number1=int(input("Please enter the first number:"))
number2=int(input("Please enter the second number:"))
sum=number1+number2
product=number1*number2
print("The sum of the numbers:",sum)
print("The product of the numbers:",product)

Question6: Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.
number1=int(input("Please enter the first number:"))
number2=int(input("Please enter the second number:))
number3=int(input("Please enter the third number:))
number4=int(input("Please enter the forth number:))
sum=number1+number2+number3+number4
mean=sum/4
print("The sum of the numbers is",sum,"and the mean is",mean)

Question7: Please write a program which estimates a user's typical food expenditure.The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week. Based on this information the program calculates the user's typical food expenditure both weekly and daily.
cafeteria_meals = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery_spending = float(input("How much money do you spend on groceries in a week? "))
weekly_total = (cafeteria_meals * lunch_price) + grocery_spending
daily_average = weekly_total / 7
print("\nAverage food expenditure:")
print("Daily:",daily_average,"euros")
print("Weekly:",weekly_total,"euros")

Question8: Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
groups = students // group_size
if students % group_size != 0:
    groups += 1
print("Number of groups formed:",groups)
