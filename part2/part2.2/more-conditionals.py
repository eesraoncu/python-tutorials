Question1: Please write a program which asks the user for their age. The program should then print out a message based on whether the user is of age or not, using 18 as the age of maturity.
age=int(input("How old are you?"))
if age>=18:
  print("You are of age!")
else:
  print("You are not of age!")

Question2: Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.
number1=int(input("Please type in the first number:"))
number2=int(input("Please type in another number:"))
if number1>number2:
  print("The greater number was:",number1)
elif number2>number1:
  print("The greater number was:",number2)
else:
  print("The numbers are equal!")

Question3: Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.
person1_name=input("Name:")
person1_age=int(input("Age:"))
person2_name=input("Name:")
person2_age=int(input("Age:"))
if person1_age>person2_age:
  print(person1_name)
elif person2_age>person1_age:
  print(person2_name)
else:
  print(person1_name,"and",person2_name,"are the same age.")

Question4: Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")
if word1 == word2:
    print("You gave the same word twice.")
elif word1 > word2:
    print(word1,"comes alphabetically last.")
else:
    print(word2,"comes alphabetically last.")
                                                    
