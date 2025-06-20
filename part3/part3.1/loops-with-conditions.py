Question1: Please write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.
number=2
while number<=30:
  print(number)
  number+=2

Question2: The program below has some syntactic issues. Please fix it.
*Wrong State*                                                     *Correct State*
print("Are you ready?")                                           print("Are you ready?")
number = int(input("Please type in a number: "))                  number = int(input("Please type in a number: "))
while number = 0:                                                 while number = 0:
print(number)                                                           print(number)
print("Now!")                                                           number-=1
                                                                  print("Now!")

Question3: Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.
upper_limit=int(input("Upper limit:"))
number=1
while number<upper_limit:
  print(number)
  number+=1

Question4: Please write a program which asks the user to type in an upper limit. The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. That is, the program prints out powers of two in order. The execution of the program finishes when the next number to be printed would be greater than the limit set by the user. No numbers greater than the limit should be printed.
upper_limit=int(input("Upper limit:"))
number=1
while number<upper_limit:
  print(number)
  number*=2

Question5: Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).
upper_limit=int(input("Upper limit:"))
base=int(input("Base:"))
number=1
while number<upper_limit:
  print(number)
  number*=base

Question6: Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. 
limit=int(input("Limit:"))
total=0
number=1
while total<limit:
  total+=number
  number+=1
print(total) 

Question7: Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed.
limit = int(input("Limit: "))
total = 0
number = 1
calculation = "1"
total += 1
while total < limit:
    number += 1
    total += number
    calculation += " + " + str(number)
print("The consecutive sum:",calculation,"=",total)
